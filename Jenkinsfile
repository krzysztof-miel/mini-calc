pipeline {
  agent any
  options { timestamps() }

  // Parametry (łatwo zmienisz wartości z UI Jenkinsa)
  parameters {
    string(name: 'PERF_USERS',    defaultValue: '10',  description: 'Liczba użytkowników (Locust -u)')
    string(name: 'PERF_SPAWN',    defaultValue: '5',   description: 'Tempo dołączania (Locust -r, users/s)')
    string(name: 'PERF_DURATION', defaultValue: '20s', description: 'Czas testu, np. 30s/1m/5m (Locust -t)')
    string(name: 'PERF_HOST',     defaultValue: 'https://jsonplaceholder.typicode.com', description: 'Host testowany (Locust --host)')
  }

  environment {
    // Używamy wartości z parametrów
    USERS    = "${params.PERF_USERS}"
    SPAWN    = "${params.PERF_SPAWN}"
    DURATION = "${params.PERF_DURATION}"
    HOST     = "${params.PERF_HOST}"
  }

  stages {
    stage('Install dependencies') {
      steps {
        sh '''
          python3 --version
          python3 -m venv .venv
          . .venv/bin/activate
          python -m pip install --upgrade pip
          pip install -r requirements.txt
        '''
      }
    }

    stage('Run unit tests') {
      steps {
        sh '''
          . .venv/bin/activate
          mkdir -p reports
          pytest -q --maxfail=1 --disable-warnings --junitxml=reports/junit.xml
        '''
      }
    }

    stage('Performance (Locust)') {
      steps {
        sh '''
          . .venv/bin/activate
          mkdir -p reports/perf
          chmod +x scripts/run_locust.sh
          # uruchamiamy Twój skrypt; przekażemy mu parametry przez zmienne środowiskowe
          USERS=${USERS} SPAWN=${SPAWN} DURATION=${DURATION} HOST=${HOST} \
            bash scripts/run_locust.sh
        '''
      }
      post {
        always {
          archiveArtifacts artifacts: 'reports/perf/*', fingerprint: true
        }
      }
    }
  }

  post {
    always {
      junit allowEmptyResults: true, testResults: 'reports/*.xml'
      archiveArtifacts artifacts: 'reports/*.xml', fingerprint: true
    }
  }
}
