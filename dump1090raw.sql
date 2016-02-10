"CREATE EXTERNAL TABLE default.dump1090raw (
  type STRING, 
  type_code TINYINT, 
  session_id TINYINT, 
  aircraft_id SMALLINT, 
  hexident STRING, 
  flight_id INT, 
  msg_date STRING, 
  msg_time STRING, 
  log_date STRING, 
  log_time STRING, 
  callsign STRING, 
  altitude INT, 
  ground_speed INT, 
  track STRING, 
  latitude FLOAT, 
  longitude FLOAT, 
  vertical_rate INT, 
  squawk STRING, 
  alert TINYINT, 
  emergency TINYINT, 
  spi TINYINT, 
  is_on_ground TINYINT
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
WITH SERDEPROPERTIES ('serialization.format'=',', 'field.delim'=',')
STORED AS TEXTFILE
LOCATION 'hdfs://quickstart.cloudera:8020/flume/raw/dump1090'
TBLPROPERTIES ('numFiles'='1', 'COLUMN_STATS_ACCURATE'='true', 'transient_lastDdlTime'='1454720306', 'numRows'='-1', 'totalSize'='38973')"
