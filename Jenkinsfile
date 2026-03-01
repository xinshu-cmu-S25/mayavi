pipeline {
    agent any
    
    tools {
        sonarScanner 'sonar-scanner' 
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', credentialsId: 'github-repo-auth', url: 'https://github.com/xinshu-cmu-S25/mayavi'
            }
        }
        
        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('sonar-server') {
                    sh "sonar-scanner -Dsonar.projectKey=mayavi -Dsonar.sources=."
                }
            }
        }
    }
}