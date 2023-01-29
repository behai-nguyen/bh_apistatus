pipeline {
    agent any

    environment {
        PYENV_HOME = "${WORKSPACE}/venv"
    }
	
    stages {
		stage ('Check and remove existing virtualenv') {
			steps {
                echo "${PYENV_HOME}"

			    script {
    				if (fileExists("${PYENV_HOME}")) {
    					echo "${PYENV_HOME} found!"
						dir("${PYENV_HOME}") {
						    deleteDir()
						}
    				}
			    }
			}
		}
		
		stage('Create and activate virtualenv') {
		    steps {
		        sh "virtualenv $PYENV_HOME"

				dir("${WORKSPACE}") {
					sh ". venv/bin/activate"
				}
		    }
		}
				
		stage('Run editable install') {
		    steps {
		        sh "$PYENV_HOME/bin/pip install -e ."
		    }
		}
		
		stage('Run pytest') {
		    steps {
		        sh "$PYENV_HOME/bin/pytest"
		    }
		}		
    }
}