(function(w,d,s,g,js,fjs){
  g=w.gapi||(w.gapi={});g.analytics={q:[],ready:function(cb){this.q.push(cb)}};
  js=d.createElement(s);fjs=d.getElementsByTagName(s)[0];
  js.src='https://apis.google.com/js/platform.js';
  fjs.parentNode.insertBefore(js,fjs);js.onload=function(){g.load('analytics')};
}(window,document,'script'));


gapi.analytics.ready(function() {

//  server auth through the token from the server
  var token = document.getElementById('token').innerHTML
  gapi.analytics.auth.authorize({
    'serverAuth': {
      'access_token': token
    }
  });

// creating one by one all charts
  var timeline_sessions = new gapi.analytics.googleCharts.DataChart({
    query: {
      'ids': 'ga:182027835', // <-- Replace with the ids value for your view.
      'start-date': '30daysAgo',
      'end-date': 'yesterday',
      'metrics': 'ga:sessions,ga:users',
      'dimensions': 'ga:date'
    },
    chart: {
      'container': 'timeline',
      'type': 'LINE',
      'options': {
        title: 'Amount of Users And Sessions',
        width: '100%'
      }
    }
  });
  timeline_sessions.execute();

  var session_map = new gapi.analytics.googleCharts.DataChart({
    query: {
      'dimensions': 'ga:country',
      'metrics': 'ga:sessions',
      'start-date': '30daysAgo',
      'end-date': 'yesterday',
      'ids': "ga:182027835",
    },
    chart: {
      type: 'GEO',
      container: 'session_map',
      options: {
        title: 'Session Geo',
        fontSize: 12,
        width: '100%'
        }
    }
  });
  session_map.execute();

  var session_duration_line = new gapi.analytics.googleCharts.DataChart({
    reportType: 'ga',
    query: {
      'dimensions': 'ga:date',
      'metrics': 'ga:avgSessionDuration',
      'start-date': '30daysAgo',
      'end-date': 'yesterday',
      'ids': "ga:182027835",
    },
    chart: {
      type: 'LINE',
      container: 'session_duration_line',
      options: {
        title: 'Average Session Duration',
        fontSize: 12,
        width: '100%'
        }
    }
  });
  session_duration_line.execute();


  var page_views = new gapi.analytics.googleCharts.DataChart({
    query: {
      'dimensions': 'ga:date',
      'metrics': 'ga:pageviews',
      'start-date': '30daysAgo',
      'end-date': 'yesterday',
      'ids': "ga:182027835",
    },
    chart: {
      type: 'LINE',
      container: 'page_views',
      options: {
        title: 'Pages Views',
        fontSize: 12,
        width: '100%'
        }
    }
  });
  page_views.execute();
});
