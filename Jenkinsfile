#!groovy
node
{
	switch("${env.BRANCH_NAME}")
	{
		case ~/master$/:
			echo "production pipeline"
			break

		case ~/develop$/:

			echo "development pipeline"

			stage("Initialize")
			{
				echo "cleaning workspace"
				deleteDir()

				echo "downloading last version"
				checkout scm
			}

			stage("Build")
			{
				echo "building"
				sh '''
					virtualenv -p python3.5 env
					. env/bin/activate
					export APP_SETTINGS="development"
					pip install -r requirements/development.txt
					deactivate
					'''
			}

			stage("Test")
			{
				echo "testing"
				sh '''
					. env/bin/activate
					export APP_SETTINGS="development"
					python main.py &
					deactivate
					'''
			}

			stage("Deploy")
			{
				echo "deploying"
				withCredentials([file(credentialsId:"aws_devops", variable:"KEY")])
				{
					sh '''
						#!/bin/bash -l
						export TARGET="target.tar.gz"
						export DESTINATION="ubuntu@ec2-18-194-55-151.eu-central-1.compute.amazonaws.com"
						export DEPLOY_PATH="/work/dev/deploys"
						export DEPLOY_DEST="python"
						export DEPLOY_SCRIPT="dev-deploy-host"

						echo "1key" $KEY
						echo "2key" ${KEY}
						
						tar --exclude='.git' --exclude='.gitignore' --exclude='pipeline' --exclude='Jenkinsfile' -czf $TARGET .

						scp -i $KEY -o StrictHostKeyChecking=no $TARGET $DESTINATION:$DEPLOY_PATH
						scp -i $KEY -o StrictHostKeyChecking=no pipeline/$DEPLOY_SCRIPT $DESTINATION:$DEPLOY_PATH
						ssh -i $KEY -o StrictHostKeyChecking=no $DESTINATION "$DEPLOY_PATH/$DEPLOY_SCRIPT $TARGET $DEPLOY_PATH $DEPLOY_DEST $DEPLOY_SCRIPT"
						'''
				}
			}

			break

		case ~/feature.*$/:
			echo "features pipeline"
			break

		default:
			echo "branch not supervised"
			break
	}
}
