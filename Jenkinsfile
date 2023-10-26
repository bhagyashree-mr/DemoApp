pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', changelog: false, poll: false, url: 'https://github.com/bhagyashree-mr/DemoApp.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    def dockerImage = docker.build("DemoApp", "--network=host")
        
                    // Tag the Docker image
                    dockerImage.tag("latest")
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Activate virtual environment and install dependencies
                    sh 'python -m venv venv'
                    sh './venv/bin/activate' // Adjusted activation command
                    sh 'pip install -r requirements.txt'

                    // Run pytest
                    sh 'pytest tests'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Deploy the Docker image (you may push it to a registry)
                    docker.withRegistry('https://docker.io', 'dockerhub-login') {
                        // Push the Docker image
                        docker.image("DemoApp").push()
                    }
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Run the Docker container
                    docker.image("DemoApp:latest").run("--name DemoAppContainer -p 8080:8080 -d")
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline successful!'
            emailext subject: 'Pipeline Successful',
                      body: 'The pipeline has been successfully executed.',
                      to: 'drishtichauhan151@gmail.com' // Add your recipient email address
        }

        failure {
            echo 'Pipeline failed!'
            emailext subject: 'Pipeline Failed',
                      body: 'The pipeline has failed. Please check the Jenkins console output for details.',
                      to: 'drishtichauhan151@gmail.com' // Add your recipient email address
        }
    }
}
