pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('mayavi-analysis') {
                    sh 'mvn sonar:sonar' 
                }
            }
        }
    }
}