pipeline {
    agent any
    
    tools {
        'hudson.plugins.sonar.SonarRunnerInstallation' 'sonar-scanner' 
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', credentialsId: 'github-repo-auth', url: 'https://github.com/xinshu-cmu-S25/mayavi'
            }
        }
        
        stage('SonarQube Analysis') {
            steps {
                script {
                    def scannerHome = tool name: 'sonar-scanner', type: 'hudson.plugins.sonar.SonarRunnerInstallation'
                    
                    withSonarQubeEnv('sonar-server') {
                        sh "${scannerHome}/bin/sonar-scanner \
                            -Dsonar.projectKey=mayavi \
                            -Dsonar.sources=. \
                            -Dsonar.host.url=http://sonarqube-service:9000"
                    }
                }
            }
        }
    }
}