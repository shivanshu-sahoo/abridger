'use strict';

;( function ( document, window, index )
{
	var inputs = document.querySelectorAll( '.inputfile' );
	Array.prototype.forEach.call( inputs, function( input )
	{
		var label	 = input.nextElementSibling,
			labelVal = label.innerHTML;
		input.addEventListener( 'change', function( e )
		{
			var fileName = '';
			if( this.files && this.files.length > 1 )
				fileName = ( this.getAttribute( 'data-multiple-caption' ) || '' ).replace( '{count}', this.files.length );
			else
				fileName = e.target.value.split( '\\' ).pop();
			if( fileName )
				label.querySelector( 'span' ).innerHTML = fileName;
			else
				label.innerHTML = labelVal;
		});

		// Firefox bug fix
		input.addEventListener( 'focus', function(){ input.classList.add( 'has-focus' ); });
		input.addEventListener( 'blur', function(){ input.classList.remove( 'has-focus' ); });
	});
}( document, window, 0 ));


// Targets all textareas with class "txta"
let textareas = document.querySelectorAll('#text-area'),
    hiddenDiv = document.createElement('div'),
    content = null;

// Adds a class to all textareas
for (let j of textareas) {
  j.classList.add('txtstuff');
}

hiddenDiv.classList.add('txta');

// Add the styles for the hidden div
// These can be in the CSS, just remove these three lines and uncomment the CSS
hiddenDiv.style.display = 'none';
hiddenDiv.style.whiteSpace = 'pre-wrap';
hiddenDiv.style.wordWrap = 'break-word';

// Loop through all the textareas and add the event listener
for(let i of textareas) {
  (function(i) {
    // Note: Use 'keyup' instead of 'input'
    // if you want older IE support
    i.addEventListener('input', function() {
      
      // Append hiddendiv to parent of textarea, so the size is correct
      i.parentNode.appendChild(hiddenDiv);
      
      // Remove this if you want the user to be able to resize it in modern browsers
      i.style.resize = 'none';
      
      // This removes scrollbars
      i.style.overflow = 'hidden';

      // Every input/change, grab the content
      content = i.value;

      // Add the same content to the hidden div
      
      // This is for old IE
      content = content.replace(/\n/g, '<br>');
      
      // The <br ..> part is for old IE
      // This also fixes the jumpy way the textarea grows if line-height isn't included
      hiddenDiv.innerHTML = content + '<br style="line-height: 3px;">';

      // Briefly make the hidden div block but invisible
      // This is in order to read the height
      hiddenDiv.style.visibility = 'hidden';
      hiddenDiv.style.display = 'block';
      i.style.height = hiddenDiv.offsetHeight + 'px';

      // Make the hidden div display:none again
      hiddenDiv.style.visibility = 'visible';
      hiddenDiv.style.display = 'none';
    });
  })(i);
}

var csrf_token = "{{ csrf_token() }}";

$.ajaxSetup({
  beforeSend: function(xhr, settings) {
      if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
          xhr.setRequestHeader("X-CSRFToken", csrf_token);
      }
  }
});

// Toggle visibility of summary text and generate questions
function toggle_visibility(id) {
  var x = document.getElementById(id);
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}


