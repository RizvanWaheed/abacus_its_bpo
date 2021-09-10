angular.module('AppFilter', []).filter('stringfy', function() {
  return function(input) {
  	//console.log('input is start');
  	//console.log(input);
  	//console.log('input is Ends');
    return ( typeof input !== 'undefined' && input > 0 )?input.toString():0;
  };
})
.filter('ina', function () {
	return function(input) {
     return input == 1 ? 'Inactive' : 'Active -';
   }
})
.filter('ina2', function () {
	return function(input) {
     return input == 1 ? 'Deny' : 'Allow';
   }
})
.filter('itemQty', function () {
	return function (major,minor) {
		result = parseFloat(major)+parseFloat(minor);
		return result.toFixed(1); 
	};
})
.filter('range', function () {
	return function(input, min, max) {
		min = parseInt(min); //Make string input int
		max = parseInt(max);
		for (var i=min; i<=max; i++)
			input.push(i);
		return input;
	};
})
.filter('replaceScopeVar', function () {
	return function(input, searches, scope) {
		if (!searches || !scope || typeof searches.length === 'undefined' || searches.length <= 0) {
			return input;
		}
		for (var i = 0; i < searches.length; i++) {
			var searchLoop = searches[i];
			var replacLoop = scope[searchLoop];
			if (typeof scope[searchLoop] === 'undefined') {
				continue;
			}
			var re = new RegExp('{{'+searchLoop+'}}', "g");
			input = input.replace(re, replacLoop);
		}
		return input;
	};
})
.filter('htmlEntityDecode', function () {
	return function(input, quote_style) {
		return AppCore.phpjs.html_entity_decode(input);
	};
})
.filter('showInTitle', function () {
	return function(input) {
		return AppCore.phpjs.html_entity_decode(input);
	};
})
.filter('toUpperCase', function () {
	return function(input) {
		return input.toUpperCase();
	};
})
.filter('toLowerCase', function () {
	return function(input) {
		return input.toLowerCase();
	};
})
.filter('firstLetter', function () {
	return function(input) {
		if (!input) {
			return '';
		} else {
			return input.charAt(0);
		}
	};
})
.filter('limitChars', function () {
	return function(input, limit) {
		if (!input) {
			return '';
		} else {
			input = input+'';
			var len = input.length;
			if (len > limit) {
				input = input.substring(0, limit);
			}
			return input;
		}
	};
})
.filter('abbrNum', function () {
	return function(input, decPlaces) {
		if (!decPlaces) decPlaces = 0;
		var val = parseFloat(input);
		if (isNaN(val)) val = 0;
		return AppCore.abbrNum(input, decPlaces);
	};
})
.filter('cut', function() {
	return function (value, wordwise, max, tail) {
		if (!value) return '';

		max = parseInt(max, 10);
		if (!max) return value;
		if (value.length <= max) return value;

		value = value.substr(0, max);
		if (wordwise) {
			var lastspace = value.lastIndexOf(' ');
			if (lastspace != -1) {
				value = value.substr(0, lastspace);
			}
		}

		return value + (tail || ' …');
	};
})
.filter('uniqueTags', function() {
	return function(list,joinarray) {
		 if (!list) return '';
		
		if(angular.isArray(list)){
			arr = $.grep(list, function(value) {
					return $.trim(value) != "TAS";
					});
			list = list.join(joinarray);
			list = list.replace("TAS","");

		}else{
			list = list.replace("TAS","");
			//list = list.replace("Dinner","aa");
		}
		
		return list;
	}
})
.filter('i18n', ['localizedTexts', function (localizedTexts) {
    return function (text) {
        if (localizedTexts.hasOwnProperty(text)) {
            return localizedTexts[text];
        }
        return text;
    };
}]);
// angular.module('AppFilter').value('localizedTexts', {});