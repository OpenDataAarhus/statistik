#sudo -i
cd /usr/lib/ckan/default/src/ckan/
. /usr/lib/ckan/default/bin/activate
paster tracking export /home/deploy/bin_script/statistics/stats.csv -c /home/deploy/bin_script/statistics/production.ini
python /home/deploy/bin_script/statistics/csv2ckan.py
