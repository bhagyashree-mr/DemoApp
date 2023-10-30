pipeline {
    agent any
    
    environment {
        PYENV_HOME = 'C:\\Program Files\\pyenv'
        PATH = "${PYENV_HOME}\\bin:${PATH}"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', changelog: false, poll: false, url: 'https://github.com/bhagyashree-mr/DemoApp.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                script {
                    // Install pyenv
                    bat 'git clone https://github.com/pyenv-win/pyenv-win.git ${PYENV_HOME}'
                    
                    // Add pyenv to PATH
                    bat 'echo export PATH="${PYENV_HOME}\\bin:$PATH" >> $PROFILE'
                    bat 'echo pyenv rehash --shim >> $PROFILE'
                    
                    // Initialize pyenv
                    bat 'pyenv --version'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    def dockerImage = docker.build("demoapp", "--network=host .")
            
                    // Tag the Docker image
                    dockerImage.tag("latest")
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Store current workspace directory in projectPath variable
                    def projectPath = pwd()

                    // Change to the project directory
                    dir(projectPath) {
                        // Activate pyenv
                        bat 'pyenv exec 3.12 python -m venv venv'
                        bat 'call .\\venv\\Scripts\\activate && echo Virtual environment activated'
                
                        // Install dependencies
                        bat "pyenv exec 3.12 pip install -r ${projectPath}\\requirements.txt"
                
                        // Run pytest
                        bat "pyenv exec 3.12 pytest ${projectPath}\\tests"
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Deploy the Docker image (you may push it to a registry)
                    docker.withRegistry('https://docker.io', 'dockerhub-login') {
                        // Push the Docker image
                        docker.image("demoapp").push()
                    }
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Run the Docker container
                    def container = docker.image("demoapp:latest").run("-p 8080:8080 --rm -d --name DemoAppContainer")
   
                    // Wait for the application to be ready (adjust the log message)
                    container.waitForLog("Application started", 60)
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline successful!'
            emailext subject: 'Pipeline Successful',
                      body: 'The pipeline has been successfully executed.',
                      to: 'pdacse80@gmail.com' // Add your recipient email address
        }

        failure {
            echo 'Pipeline failed!'
            emailext subject: 'Pipeline Failed',
                      body: 'The pipeline has failed. Please check the Jenkins console output for details.',
                      to: 'pdacse80@gmail.com' // Add your recipient email address
        }
    }
}
