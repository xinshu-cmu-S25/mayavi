pipeline {
  agent any

  tools {
    'hudson.plugins.sonar.SonarRunnerInstallation' 'sonar-scanner'
  }

  environment {
    SONAR_HOST_URL = 'http://sonarqube-service.default.svc.cluster.local:9000'
  }

  stages {
    stage('Checkout') {
      steps {
        git branch: 'main',
            credentialsId: 'github-repo-auth',
            url: 'https://github.com/xinshu-cmu-S25/mayavi'
      }
    }

    stage('Wait for SonarQube') {
      steps {
        sh '''
          for i in $(seq 1 60); do
            resp=$(curl -s ${SONAR_HOST_URL}/api/system/status || true)
            echo "$resp" | grep -q '"status":"UP"' && exit 0
            sleep 3
          done
          echo "SonarQube not UP in time" >&2
          exit 1
        '''
      }
    }

    stage('SonarQube Analysis') {
      steps {
        script {
          def scannerHome = tool name: 'sonar-scanner', type: 'hudson.plugins.sonar.SonarRunnerInstallation'

          withCredentials([string(credentialsId: 'sonar-token', variable: 'SONAR_TOKEN')]) {
            sh '''
              set -euo pipefail
              echo "Sanity check SonarQube auth..."
              curl -s -o /dev/null -w "HTTP %{http_code}\n" -u "${SONAR_TOKEN}:" ${SONAR_HOST_URL}/api/v2/analysis/version

              echo "Running sonar-scanner..."
              '"${scannerHome}"'/bin/sonar-scanner \
                -Dsonar.projectKey=mayavi \
                -Dsonar.sources=. \
                -Dsonar.host.url=${SONAR_HOST_URL} \
                -Dsonar.token=${SONAR_TOKEN}
            '''
          }
        }
      }
    }
  }
}
