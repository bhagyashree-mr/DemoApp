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
                    // Check if pyenv directory exists
                    if (!fileExists(PYENV_HOME)) {
                        // Clone pyenv repository
                        bat 'git clone https://github.com/pyenv-win/pyenv-win.git "${PYENV_HOME}"'
                    }
                    
                    // Add pyenv to PATH
                    bat 'echo export PATH="${PYENV_HOME}\\bin:$PATH" >> ${env.USERPROFILE}\\Documents\\WindowsPowerShell\\profile.ps1'
                    bat 'echo pyenv rehash --shim >> ${env.USERPROFILE}\\Documents\\WindowsPowerShell\\profile.ps1'
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
                        // Ensure pyenv is available in the current session
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
                    // Deploy the Docker image to Docker Hub
                    docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-login') {
                        // Push the Docker image
                        docker.image("bhagyashreemreddy/demoapp").push()
                    }
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Run the Docker container
                    def container = docker.image("bhagyashreemreddy/demoapp:latest").run("-p 8080:8080 --rm -d --name DemoAppContainer")
   
                    // Wait for the application to be ready (adjust the log message)
                    container.waitForLog("Your application-specific log message indicating that it has started", 60)
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
