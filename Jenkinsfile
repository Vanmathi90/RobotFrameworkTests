pipeline {
    agent any
    environment {
        ROBOT_BROWSER_OPTIONS = "/tmp/chrome-${BUILD_ID}"
        VENV = "${WORKSPACE}/venv"
        DIR_PATH = "/home/vanmathiganesan/RobotFrameworkTests/robot-tests/reports/${BUILD_ID}/"
        HTML_DIR_PATH = "/home/vanmathiganesan/RobotFrameworkTests/robot-tests/reports/${BUILD_ID}/index.html"
        TABLE_DIR_PATH = "/home/vanmathiganesan/RobotFrameworkTests/robot-tests/reports/${BUILD_ID}/table.png"
        REPORT_DIR_PATH = "/home/vanmathiganesan/RobotFrameworkTests/robot-tests/reports/${BUILD_ID}/report.png"
    }
    stages {
        stage('Git Checkout') {
            steps {
                echo 'Pulling latest Robot Code from Git'
                git branch 'main', 'https://github.com/Vanmathi90/RobotFrameworkTests.git'
            }
        }
        stage('Setup Virtual Environment') {
            steps {
                echo 'Setting Python Virtual Environment'
                sh '''
                    python3 -m venv ${VENV}
                    pip3 install -r requirements.txt
                '''
            }
        }
        stage('Run Robot Framework Tests') {
            steps {
                echo 'Running Robot Framework Tests'
                sh '''
                    mkdir reports/{BUILD_ID}
                    . ${VENV}/bin/activate
                    python3 -m robot --variable ROBOT_BROWSER_OPTIONS:${ROBOT_BROWSER_OPTIONS} -d reports/${BUILD_ID}/ tests/basic_test.robot
                '''
            }
        }
        stage ('Generate Report Graphs') {
            steps {
                echo 'Generating HTML Report Graphs'
                sh '''
                    . ${VENV}/bin/activate
                    python3 generate_report.py ${BUILD_ID}
                '''
            }
        }
        stage ('Generate HTML Report'){
            steps {
                echo 'Generating HTML report in jenkins'
                sh '''
                    cat > ${HTML_DIR_PATH} <<EOF
                    <!DOCTYPE html>
                    <html>
                    <head>
                      <meta charset="utf-8">
                      <title>Test Run Report</title>
                    </head>
                    <body>
                      <h2> Test Run Report based by Requirements </h2>
                      <img src="${TABLE_DIR_PATH}" alt="Test Run Report Table">
                      </br>
                      <img src="${REPORT_DIR_PATH}" alt="Test Run Report Chart">
                    </body>
                    </html>
                    EOF
                '''
            }
        }
    }
    post {
        success {
            publishHTML([
			  reportDir: '${DIR_PATH}',
			  reportFiles: 'index.html',
			  reportName: 'Test Run Report',
			  keepAll: true,
			  alwaysLinkToLastBuild: true,
			  allowMissing: false
			])
        }
    }
}