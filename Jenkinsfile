// Use a specific Python version with the Docker Pipeline plugin
pipeline {
    agent {
        docker {
            image 'python:3.12-slim'
        }
    }

    // Defines the different stages of the pipeline
    stages {
        // Stage 1: Checkout the code from your repository
        stage('Checkout') {
            steps {
                echo 'Checking out the code...'
                // The 'checkout scm' command automatically pulls the code
                // from the repository configured in the Jenkins job.
                checkout scm
            }
        }

        // Stage 2: Install dependencies and build
        stage('Build') {
            steps {
                echo 'Installing dependencies...'
                sh 'pip install -r requirements.txt'
            }
        }

        // Stage 3: Run automated tests
        stage('Test') {
            steps {
                echo 'Running automated tests...'
                sh 'python -m unittest test_app.py'
            }
        }
    }

    // Actions to perform after all stages have completed
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
