SELECT LAST("pm1") FROM "aqi_real"."autogen"."aqi" WHERE time > :dashboardTime: AND time < :upperDashboardTime: 

SELECT LAST("pm2.5") FROM "aqi_real"."autogen"."aqi" WHERE time > :dashboardTime: AND time < :upperDashboardTime: 

SELECT LAST("pm10") FROM "aqi_real"."autogen"."aqi" WHERE time > :dashboardTime: AND time < :upperDashboardTime: 

SELECT mean("pm1") AS "pm1", mean("pm10") AS "pm10", mean("pm2.5") AS "pm2.5" FROM "aqi_real"."autogen"."aqi" WHERE time > :dashboardTime: AND time < :upperDashboardTime: GROUP BY time(:interval:) FILL(-1)