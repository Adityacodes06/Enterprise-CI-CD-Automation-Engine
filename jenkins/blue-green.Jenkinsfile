// Blue-Green deployment pipeline - standalone stage for deployment only
pipeline {
    agent any

    parameters {
        choice(
            name: 'DEPLOY_TARGET',
            choices: ['blue', 'green'],
            description: 'Environment to promote to production'
        )
        string(
            name: 'IMAGE_TAG',
            defaultValue: 'latest',
            description: 'Docker image tag to deploy'
        )
    }

    stages {
        stage('Promote to Production') {
            steps {
                sh '''
                    ./scripts/blue-green-deploy.sh promote ${params.DEPLOY_TARGET} ${params.IMAGE_TAG}
                '''
            }
        }
    }
}
