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
        
                    // Create the directory for PowerShell profile
                    mkdir "${env.USERPROFILE}\\Documents\\WindowsPowerShell"
        
                    // Add pyenv to PATH
                    bat 'echo export PATH="${PYENV_HOME}\\bin:$PATH" >> "${env.USERPROFILE}\\Documents\\WindowsPowerShell\\profile.ps1"'
                    bat 'echo pyenv rehash --shim >> "${env.USERPROFILE}\\Documents\\WindowsPowerShell\\profile.ps1"'
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
    }

    post {
        success {
            echo 'Pipeline successful!'
        }

        failure {
            echo 'Pipeline failed!'
        }
    }
}
