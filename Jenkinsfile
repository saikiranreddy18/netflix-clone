pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "dsai18/netflix-clone:${BUILD_NUMBER}"
    }

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/saikiranreddy18/netflix-clone.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build(DOCKER_IMAGE)
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                script {
                    sh '''
                        echo "Logging in to DockerHub..."
                        docker login -u dsai18 -p sai.T123\\$
                        echo "Pushing Docker image..."
                        docker push dsai18/netflix-clone:$BUILD_NUMBER
                    '''
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    sh """
                        helm upgrade --install netflix-clone ./helm-chart \
                          --set image.repository=dsai18/netflix-clone \
                          --set image.tag=${BUILD_NUMBER}
                    """
                }
            }
        }
    }
}
