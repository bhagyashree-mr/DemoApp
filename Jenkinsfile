pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', changelog: false, poll: false, url: 'htpipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', changelog: false, poll: false, url: 'https://github.com/bhagyashree-mr/DemoApp.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    def dockerImage = docker.build("demoapp", "--network=host .") // Add the build context (.)
            
                    // Tag the Docker image
                    dockerImage.tag("latest")
                }
            }
        }
        
        stage('Run Tests') {
    steps {
            script {
                // Change to the project directory
                dir('C:\\Users\\bande\\OneDrive\\Desktop\\Dockers\\Projects\\demoWebApp') {
                    // Create and activate virtual environment
                    bat 'C:\\Users\\bande\\AppData\\Local\\Programs\\Python\\Python312\\python -m venv venv'
                    bat 'call .\\venv\\Scripts\\activate && echo Virtual environment activated'
            
                    // Install dependencies
                    bat 'C:\\Users\\bande\\AppData\\Local\\Programs\\Python\\Python312\\venv\\Scripts\\pip install -r C:\\Users\\bande\\OneDrive\\Desktop\\Dockers\\Projects\\demoWebApp\\requirements.txt'
            
                    // Run pytest using the full path to Python executable
                    bat 'C:\\Users\\bande\\AppData\\Local\\Programs\\Python\\Python312\\venv\\Scripts\\pytest  C:\\Users\\bande\\OneDrive\\Desktop\\Dockers\\Projects\\demoWebApp\\tests'
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
tps://github.com/bhagyashree-mr/DemoApp.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    def dockerImage = docker.build("demoapp", "--network=host .") // Add the build context (.)
            
                    // Tag the Docker image
                    dockerImage.tag("latest")
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Change to the project directory
                    dir('C:\\Users\\bande\\AppData\\Local\\Programs\\Python\\Python312\\python') {
                        // Create and activate virtual environment
                        bat 'C:\\Users\\bande\\AppData\\Local\\Programs\\Python\\Python312\\python -m venv venv'
                        bat '.\\venv\\Scripts\\activate && echo Virtual environment activated'
                
                        // Install dependencies
                        bat '.\\venv\\Scripts\\pip install -r requirements.txt'
                
                        // Run pytest using the full path to Python executable
                        bat '.\\venv\\Scripts\\pytest tests'
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
