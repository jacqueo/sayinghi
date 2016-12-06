# How to use Git and Github

# Step 1: initialize Git in the proper workplace (i.e. git init inside certain folder)
     #use code: git init
# Step 2: add the code to git (i.e. part 1 of 2 in saving with Git)
     #use code: git add .
# Step 3: commit the code to Git (i.e. whatever is there, freeze that and save it into a stored Git server)
     #use code: git commit (optional: -m 'inital commit') -m denotes a comment, 'enter comment here'
# Step 4: push onto Github (i.e. send the actual code to Github's servers)
     #use code: git push -u origin master (still don't know what -u does, or origin master refers to)
# Step 4: check any step of this process with git status
	#use code: git status






"""


…or create a new repository on the command line

echo "# unitOne" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/jacqueo/unitOne.git
git push -u origin master
…or push an existing repository from the command line

git remote add origin https://github.com/jacqueo/unitOne.git
git push -u origin master
…or import code from another repository
You can initialize this repository with code from a Subversion, Mercurial, or TFS project.

"""