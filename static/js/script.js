// JavaScript Document
$(document).ready(function() {
						   $('.player_name_div').delay(500).slideDown('slow');
						   $('.close_bt,.rules_content').hide();
						   var check=0;
						   $('.button').bind("click",function() {
															  if(check==0)
															  {
																  $('.rules_div').animate({width:"20%"},function() {
																  $('.close_bt,.rules_content').fadeIn();});
																 
																  check=1;
															  }
															  else if(check==1)
															  {
																  $('.close_bt,.rules_content').hide();
																  $('.rules_div').delay(100).animate({width:"0%"});
																  
																  check=0;
															  }
															  });
						   $('.close_bt').click(function() {
														  $('.close_bt,.rules_content').hide();
														  $('.rules_div').animate({width:"0%"});
																 
																  check=0;
														 });
						   });