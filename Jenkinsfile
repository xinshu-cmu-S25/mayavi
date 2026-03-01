pipeline {
    agent any
    
    tools {
        'sonar-scanner' 'sonar-scanner' 
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('sonar-server') {
                    sh 'sonar-scanner' 
                }
            }
        }
    }
}