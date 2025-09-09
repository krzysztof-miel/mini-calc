pipeline {
  agent any
  options { timestamps() }

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

    stage('Run tests') {
      steps {
        sh '''
          . .venv/bin/activate
          mkdir -p reports
          pytest -q --maxfail=1 --disable-warnings --junitxml=reports/junit.xml
        '''
      }
    }
  }

  post {
    always {
      junit 'reports/*.xml'
      archiveArtifacts artifacts: 'reports/*.xml', fingerprint: true
    }
  }
}
