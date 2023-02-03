from prefect.filesystems import GitHub

github_block = GitHub.load("prefect-github")

flow.deploy(name="Prefect Github",storage=github_block)




