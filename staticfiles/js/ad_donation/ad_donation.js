$(document).ready(function(){
    $("iframe").attr("id","existing-iframe-example")
//    atr_src = $('iframe').attr('src')+"&enablejsapi=1"
    atr_src = $('iframe').attr('src')+"&enablejsapi=1&modestbranding=1&autohide=1&showinfo=0&controls=0&rel=0&disablekb=1"
    $("iframe").attr("src",atr_src)
    $("iframe").removeAttr("allowfullscreen");
    console.log(atr_src);
	
    $("#donate").click(function(){
        $.ajax({
            type:"GET",
            url: 'donate/',
            data: {
                csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
                'from_page':"this is came from the page",
				'video_pk':$("#video_pk").html()
            },
            success: function(result){
                    $("#don_amount").html(result.total_don_from_users);
                    $("#you_just_donated").html(" You just earned $ 0.1!! Money remaine: $"+result.don_from_users);
                    $("#donate").addClass("hidden");
                    $("#donate_arrows").addClass("hidden");
                    $("#next_video").removeClass("hidden");
                    $("#you_just_donated").removeClass("invisible");
                    $("#next_video_arrows").removeClass("hidden");
					$(".progress-bar").css({"width":result.project_progress+"%"});
					$(".label_progress").html(result.project_progress+"%");
					$("#donated").html(result.project_donations);
            }
        })
    })
})

var tag = document.createElement('script');
  tag.id = 'iframe-demo';
  tag.src = 'https://www.youtube.com/iframe_api';
  var firstScriptTag = document.getElementsByTagName('script')[0];
  firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

  var player;
  function onYouTubeIframeAPIReady() {
    player = new YT.Player('existing-iframe-example', {
        events: {
          'onReady': onPlayerReady,
          'onStateChange': onPlayerStateChange
        }
    });
	

  }
  function onPlayerReady(event) {
	$(window).blur(function() {
		player.pauseVideo();
	});
    console.log("ready");
		
  }

  function onPlayerStateChange(event) {
    if (event.data==0){
         $("#donate").removeClass("invisible");
         $("#donate_arrows").removeClass("invisible");
//         alert ($("#donate").offset().top);
         $('html, body').animate({
            scrollTop: ($('#donate').offset().top)
        },1000);
    }
	
	if (event.data==1){
		$(window).focus();
    }
	
  }
  
  
