$(function()  {
	$("a.language").on("click", function(){
		$("#lang_input").val($(this).attr("val"));
		changeLanguage();
	});
});

function changeLanguage() {
	$("#lang_button").trigger("click");
}
