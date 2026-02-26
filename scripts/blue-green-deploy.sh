#!/bin/bash
# Blue-Green Deployment Script for CI/CD Automation Engine
# Usage:
#   Initial deploy: ./blue-green-deploy.sh <workspace> <app_name> <image_tag>
#   Promote:        ./blue-green-deploy.sh promote <blue|green> <image_tag>

set -e

DEPLOY_DIR="${DEPLOY_DIR:-/opt/deployments}"
BLUE_DIR="${DEPLOY_DIR}/blue"
GREEN_DIR="${DEPLOY_DIR}/green"
ACTIVE_LINK="${DEPLOY_DIR}/current"

determine_target() {
    if [ -L "$ACTIVE_LINK" ]; then
        current=$(readlink "$ACTIVE_LINK")
        if [[ "$current" == *"blue"* ]]; then
            echo "green"
        else
            echo "blue"
        fi
    else
        echo "blue"
    fi
}

deploy_to() {
    local target=$1
    local workspace=$2
    local app_name=$3
    local image_tag=$4
    local target_dir

    if [ "$target" == "blue" ]; then
        target_dir="$BLUE_DIR"
    else
        target_dir="$GREEN_DIR"
    fi

    mkdir -p "$target_dir"
    echo "Deploying $app_name:$image_tag to $target..."

    # Simulated deployment - in production: docker compose, k8s, or EC2 update
    echo "{\"image\": \"$app_name:$image_tag\", \"deployed_at\": \"$(date -Iseconds)\", \"target\": \"$target\"}" > "$target_dir/deployment.json"
    cp -r "$workspace/app"/* "$target_dir/" 2>/dev/null || true

    echo "Deployment to $target complete."
}

switch_traffic() {
    local new_active=$1
    local active_dir

    if [ "$new_active" == "blue" ]; then
        active_dir="$BLUE_DIR"
    else
        active_dir="$GREEN_DIR"
    fi

    rm -f "$ACTIVE_LINK"
    ln -s "$active_dir" "$ACTIVE_LINK"
    echo "Traffic switched to $new_active."
}

# Main
case "${1:-}" in
    promote)
        TARGET=$2
        IMAGE_TAG=${3:-latest}
        if [ -z "$TARGET" ]; then
            echo "Usage: $0 promote <blue|green> [image_tag]"
            exit 1
        fi
        switch_traffic "$TARGET"
        ;;
    *)
        WORKSPACE=$1
        APP_NAME=$2
        IMAGE_TAG=$3

        if [ -z "$WORKSPACE" ] || [ -z "$APP_NAME" ]; then
            echo "Usage: $0 <workspace> <app_name> <image_tag>"
            echo "   or: $0 promote <blue|green> [image_tag]"
            exit 1
        fi

        TARGET=$(determine_target)
        deploy_to "$TARGET" "$WORKSPACE" "$APP_NAME" "${IMAGE_TAG:-latest}"
        switch_traffic "$TARGET"
        ;;
esac
