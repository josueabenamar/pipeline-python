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
				sh "./pipeline/dev-build"
			}

			stage("Test")
			{
				echo "testing"
				sh "./pipeline/dev-test"
			}

			stage("Deploy")
			{
				echo "deploying"
				sh "./pipeline/dev-deploy"
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
