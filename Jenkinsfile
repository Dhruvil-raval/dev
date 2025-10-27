// Corrected Jenkinsfile
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
                echo 'Installing dependencies...'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'Running automated tests...'
                sh 'python -m unittest test_app.py'
            }
        }
    }
    
    // The post block must contain conditions with steps
    post {
        always {
            echo 'Pipeline execution complete.'
        }
        success {
            echo 'The pipeline finished successfully!'
        }
        failure {
            echo 'The pipeline failed. Check the logs for details.'
        }
    }
}
