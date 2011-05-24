import os

from fabric.api import local, lcd

projects = {'pycalendar': 'http://svn.mulberrymail.com/repos/PyCalendar/'
                          'branches/server-stable@161',
            'kerberos': 'http://svn.calendarserver.org/repository/'
                          'calendarserver/PyKerberos/trunk@7357',
            'calendarserver':  'http://svn.macosforge.org/repository/'
                               'calendarserver/CalendarServer/trunk@7257'}


def get_svn_export(project, url):
    """Get the svn export from a given url."""

    project_dir = os.path.join('/tmp', project)
    local('rm -rf {project_dir}'.format(project_dir=project_dir))
    local('svn co "{url}" {project_dir}'.format(url=url, 
                                                project_dir=project_dir))
    
def build_tar(project):
    """Build the tar for the project."""

    project_dir = os.path.join('/tmp', project)
    with lcd(project_dir):
        version = local('python setup.py --version', capture=True)
        version = version.replace(' ', '')
    project_version = '{project}-{version}'.format(project=project,
                                                       version=version)
    new_project_dir = os.path.join('/tmp', project_version)
    local('rm -rf "{new_project_dir}"'.format(new_project_dir=new_project_dir))
    local('svn export "{project_dir}" "{new_project_dir}"'.format(
        project_dir=project_dir, new_project_dir=new_project_dir))
    with lcd(new_project_dir.replace('(','\(').replace(')','\)')):
        # Clean up development left overs
        local('rm -f .project')
        local('rm -f .pydevproject')

    #Tar
    project_tar = project_version + '.tar.gz'
    local('tar -C /tmp -czvf "{project_tar}" '
          '"{project_version}"'.format(project_version=project_version,
                                       project_tar=project_tar))
    local('sha256sum "{project_tar}" |awk \'{{printf "SHA256 (%s) = %s\\n", $2, $1 }}\' > distinfo'.format(project_tar=project_tar))
    local('ls -l "{project_tar}" |awk \'{{printf "SIZE (%s) = %s\\n", $8, $5 }}\' >> distinfo'.format(project_tar=project_tar))


def build(project):
    project_url = projects[project]
    get_svn_export(project, project_url)
    build_tar(project)
