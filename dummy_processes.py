# Author: Sezer Yavuzer Bozkir <admin@sezerbozkir.com>
# License: The GNU General Public License v3.0
# Created Date: 24.08.2017
# Version: 0.1
# Website: https://github.com/Natgho/Flask-user-system

from db_conf import create_dummy_countries, create_dummy_users

if __name__ == '__main__':
    # Create dummy countries
    create_dummy_countries()
    # Create dummy users
    create_dummy_users()
