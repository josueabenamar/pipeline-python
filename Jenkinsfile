#!groovy
node
{
	switch("${env.BRANCH_NAME}")
	{
		case ~/master$/:

			echo "production pipeline"
			sh "./pipeline/config-prod"

			break

		case ~/develop$/:

			echo "development pipeline"

			stage("Initialize")
			{
				echo "cleaning workspace"
				deleteDir()

				echo "downloading last version"
				checkout scm

				echo "initializing"
				sh "./pipeline/config-dev"
				sh "./pipeline/process-init"
			}

			stage("Build")
			{
				echo "building"
				sh "./pipeline/process-build"
			}

			stage("Test")
			{
				echo "testing"
				sh "./pipeline/process-test"
			}

			stage("Deploy")
			{
				echo "deploying"
				sh "./pipeline/process-deploy"
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
