pipeline{
    agent {label 'worker'}		
    options{										
        buildDiscarder(logRotator(daysToKeepStr: '7'))
        disableConcurrentBuilds()
        timeout(time: 3, unit : 'MINUTES')
        retry(3)
    }
    parameters{											
        choice(name: 'choice', choices: ['start', 'stop'])
    }
    stages{											
        stage("Build"){
            steps{
                cleanWs()
				checkout scm
            }
        }
        stage("Install python"){
            steps{
                sh "sudo apt-get update -y"
                sh "sudo apt-get install python3 -y"
				sh "sudo apt-get install python3-pip -y"
				sh "pip3 install boto3"
				sh "sleep 10"
            }
        }
		stage("Start/Stop"){
            steps{
                sh "python3 ec2StartStop.py $choice"
            }
        }
    }
}
