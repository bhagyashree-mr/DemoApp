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
            def pyenvCloneDir = 'C:\\Program Files\\pyenv'
            def profilePath = "${env.USERPROFILE}\\Documents\\WindowsPowerShell\\profile.ps1"

            // Check if pyenv directory exists
            if (!fileExists(pyenvCloneDir)) {
                // Clone pyenv repository
                bat "git clone https://github.com/pyenv-win/pyenv-win.git \"${pyenvCloneDir}\""
            } else {
                // Update existing clone
                dir(pyenvCloneDir) {
                    bat 'git pull origin master'
                }
            }

            // Create directories if they don't exist
            bat 'mkdir %USERPROFILE%\\Documents\\WindowsPowerShell'
            bat 'echo. > %USERPROFILE%\\Documents\\WindowsPowerShell\\profile.ps1'

            // Add pyenv to PATH
            bat "echo export PATH=\"${pyenvCloneDir}\\bin:$PATH\" >> ${profilePath}"
            bat "echo pyenv rehash --shim >> ${profilePath}"
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
                        bat 'refreshenv'
                
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

        // Add other stages as needed...

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
