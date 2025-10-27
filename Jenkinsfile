// Updated Jenkinsfile to run pip install as root
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out the code...'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Installing dependencies as root...'
                script {
                    // Find the ID of the current Jenkins container
                    def containerId = sh(returnStdout: true, script: "docker ps -q --filter ancestor=jenkins/jenkins:lts").trim()
                    // Execute pip install command as root inside the container
                    sh "docker exec -u root \$containerId pip install -r requirements.txt"
                }
            }
        }

        stage('Test') {
            steps {
                echo 'Running automated tests...'
                sh 'python -m unittest test_app.py'
            }
        }
    }

    post {
        // ...
    }
}
