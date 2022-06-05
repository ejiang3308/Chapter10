pipeline {
<<<<<<< HEAD
    agent any;
    stages {
        stage('Preparing the environment') {
            steps {
                sh 'python3 -m install -r requirements.txt'
            }
        }
        stage('Code Quality') {
            steps {
                sh 'python3 -m pylint app.py'

            }
        }
        stage('Tests') {
            steps {
                sh 'python3 -m pytest'
                }
            }
        stage('Build') {
            steps {
                sh 'exit 1'
                }
            }
        stage('Delivery') {
            steps {
                sh 'exit 1'
                }
            }
        stage('Deploy') {
            steps {
                sh 'exit 1'
                }
            }
        }
    }
=======
  agent any
  stages {
    stage('Code Quality') {
      steps {
        sh 'echo checking code quality'
      }
    }

    stage('Unit Tests') {
      steps {
        sh 'echo Testing the Applications'
      }
    }

    stage('Build') {
      steps {
        sh 'echo Creating application Package'
      }
    }

    stage('Delivery') {
      steps {
        sh 'echo Uploading the artifact to a repository'
      }
    }

    stage('Deploy') {
      steps {
        sh 'echo Deploying the Application'
      }
    }

  }
}
>>>>>>> cefb3378db3cb07107980f9dcc9542ceaf5c3f14
