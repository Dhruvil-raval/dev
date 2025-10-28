pipeline {
    agent {
        docker {
            image 'python:3.9-slim'
        }
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out the code...'
                // This step is redundant in the log as the main pipeline directive already does a checkout.
                // However, the original log shows it happened inside a stage, so we'll keep it for fidelity.
                checkout scm
            }
        }
        
        stage('Build') {
            steps {
                echo 'Installing dependencies...'
                sh 'pip install -r requirements.txt'
            }
        }
        
        stage('Test') {
            steps {
                echo 'Running tests...'
                // Add your testing command here. For example:
                // sh 'python -m pytest'
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline execution complete.'
        }
        failure {
            echo 'The pipeline failed. Check the logs for details.'
        }
    }
}
