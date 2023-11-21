pipeline {
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
                    def dockerImage = docker.build("bhagyashreemreddy/demoapp", "--network=host .")
            
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
                        // Install dependencies
                        bat "${projectPath}\\venv\\Scripts\\pip install -r ${projectPath}\\requirements.txt"
                
                        // Run pytest
                        bat "${projectPath}\\venv\\Scripts\\python -m pytest ${projectPath}\\tests"
                    }
                }
            }
        }


        stage('Deploy') {
            steps {
                script {
					withDockerRegistry(credentialsId: 'dockerhub-login')  {
                        // Push the Docker image
                        docker.image("bhagyashreemreddy/demoapp").push()
                    }
                }
            }
        }

        stage('Run the Application') {
            steps {
                script {
		    // Pull the Docker image
           	     docker.image("bhagyashreemreddy/demoapp:latest").pull()
                    // Run the Docker container
                    def container = docker.image("bhagyashreemreddy/demoapp:latest").run("-p 8025:8025 --rm --name demoapp_container")
   
                    // Wait for the application to be ready (adjust the log message)
                    //container.waitForLog("Your application-specific log message indicating that it has started", 60)
                }
            }
        }
    }

   post {
    success {
        echo 'Pipeline successful!'
        emailext subject: 'Pipeline Successful',
                  body: 'The pipeline has been successfully executed.',
                  to: 'bandebhagyashree@gmail.com', // Add your recipient email address
                  attachLog: true
    }

    failure {
        echo 'Pipeline failed!'
        emailext subject: 'Pipeline Failed',
                  body: 'The pipeline has failed. Please check the Jenkins console output for details.',
                  to: 'pdacse80@gmail.com', // Add your recipient email address
                  attachLog: true
    }
 }

}
