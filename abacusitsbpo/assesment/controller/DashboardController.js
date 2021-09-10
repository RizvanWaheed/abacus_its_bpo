AssesmentModule.controller('DashboardController', ['$scope','$timeout','$routeParams', '$location', 'Svc',
	function($scope,$timeout,$routeParams,$location, Svc){
		
		$scope.contentsLoaded = false;
		$scope.PageData 	 = {};
		$scope.date 		 = currDate;
		$scope.selectDate    = currDate;
		$scope.format 		 = 'yyyy-MM-dd';
		
		// $scope.roleIDGlobal  = userRoleID;
	//	$scope.companyIDGlobal= userCompanyID;
		$scope.myRoleN		 = userRole;

		// $scope.selectedCompanyID     = userCompanyID;
		// $scope.selectedCompanyName   = userCompany;
        $scope.showPagination = false;

		//$scope.PagingHeaders  = 0;
		$scope.showCompany    = false;
		$scope.currentChild   = '';

				
		$scope.MsgData = {};
		$scope.sortObj = {
			sortby: 'name',
			sortdr: 'Asc'
		};
		$scope.page = 1;
		$scope.PagingHeaders = {};
		$scope.setPageNameData = function(a){
			$scope.pageName = a;
		}
		// $scope.setPageNameData('Dashboard');
		$scope.getCompanies = function(){
			// params = {
			// 	action: 'getDashboardCompanies.json',
			// 	company_id:$scope.selectedCompanyID
			// };
			// Svc.get(
			// 	AppCore.parseNGAjaxReq(params),
			// 	function(response) {		
			// 		if (response.data.success_status){
			// 			$scope.companies = angular.copy(response.data.companies);
			// 			//console.log(response);
			// 			//$scope.parseDashboardPageData(response);
			// 		}else{
			// 			//$scope.parseDashboardPageData(response);
			// 		}
			// 	},
			// 	function(error) {
			// 		console.log(error);
			// 		//alert(error);
			// 		return false;
			// 	}
			// );
		}
		// $scope.getCompanies();
		$scope.params = {
			action: 'getDashboardGraph.json',
			company_id:$scope.selectedCompanyID
		};
		$scope.getDashboardData = function(){
			//to send services to get Access of inner pages and companies
			//$('html').removeClass('menu-open');
			Svc.get(
				AppCore.parseNGAjaxReq($scope.params),
				function(response) {		
					if (response.data.success_status){
						$scope.parseDashboardPageData(response);
					}else{
						$scope.parseDashboardPageData(response);
					}
				},
				function(error) {
					console.log(error);
					alert(error);
					return false;
				}
			);
		};
		$scope.parseDashboardPageData = function(response){
			$scope.datewise	    = angular.copy(response.data.datewise);
			$scope.locationwise = angular.copy(response.data.locationwise);
			$scope.scorewise = angular.copy(response.data.scorewise);
			$scope.gaugewise = angular.copy(response.data.gaugewise);
			//console.log(response);
			$scope.loadDateWiseGraph();
			$scope.loadLocationsGraph();
			$scope.loadScoreWiseGraph();
			//$scope.loadGaugeWisueGraph();
			$scope.loadPieWiseGraph();
		};
		$scope.viewCompany = function(company_id){
			$scope.selectedCompanyID     = company_id;
		//    $scope.selectedCompanyName   = userCompany;
		    angular.forEach($scope.companies, function(value, key) {
				if(value.id == company_id)
					$scope.selectedCompanyName = value.name;
			});
		//	$scope.currentChild.selectedCompanyID = company_id;
			$scope.params.company_id = company_id;
			$scope.getDashboardData(); //, $scope.currentChild
		};
		//if($scope.companyIDGlobal == 1){
		//$scope.getDashboardData();
		$scope.loadPieWiseGraph =  function(){
			var chartHigh = new Highcharts.Chart({
		        chart: {
		        	 backgroundColor: '#f5f5f5',
		            plotBackgroundColor: null,
		            plotBorderWidth: 0,
		            plotShadow: false,
		             renderTo: 'container_timeline_gauge',
		        },
		        credits: {
		            enabled: false
		        },
		        title: {
		            text:'NPS <br> '+ $scope.gaugewise.pieChart.nps, //'<img src="/cem/img/LS02.png" />',
		            align: 'center',
		            verticalAlign: 'middle',
		            style:{
	                  //  fontWeight: 'bold',
                        color: 'black',
                      //  textShadow: '0px 1px 2px black',
	                    fontSize: '13px'
	                } ,
		            y: -1
		        },
		        tooltip: {
		            pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
		        },
		        plotOptions: {
		            pie: {
		                dataLabels: {
		                    enabled: true,
		                    distance: 0,
		                    style: {
		                        fontWeight: 'bold',
		                        color: 'white',
		                        textShadow: '0px 1px 2px black'
		                    }
		                },
		                startAngle: -180,
		                endAngle: 180,
		                center: ['50%', '50%']
		            }
		        },
		        series: [{
		            type: 'pie',
		            name: 'Browser share',
		            innerSize: '70%',
		            data: [
		                {
		                        id: 'detractor',
		                        name: 'Detractor',
		                        y: $scope.gaugewise.pieChart.de,
		                        points: 20,
		                        color: '#cd0200',
		                        events: {
		                            click: function(event) {
		                                this.update({
		                                    //color: "#ECB631"
		                                });
		                            }
		                        }
		                    },
		                    {
		                        id: 'passive',
		                        name: 'Passive',
		                        y: $scope.gaugewise.pieChart.pa,
		                        points: 20,
		                        color: '#d47500'                    
		                    },
		                    {
		                        id: 'promoter',
		                        name: 'Promoter',
		                        y: $scope.gaugewise.pieChart.pr,
		                        points: 20,
		                        color: '#3cb521'
		                    }
		               
		            ]
		        }]
		    });
		};
		$scope.loadGaugeWisueGraph = function(){
			var self = this;
		   	//console.log(this.get('dateWiseGraph'));
		    var chartHigh = new Highcharts.Chart({

		        chart: {
		            type: 'gauge',
		            plotBackgroundColor: null,
		            plotBackgroundImage: null,
		            plotBorderWidth: 0,
		            plotShadow: false,
		            renderTo: 'container_timeline_gauge',
			       
		        },
		        title: {
		            text: ''
		        },

		        pane: {
		            startAngle: -120,
		            endAngle: 120,
		            background: [{
		                backgroundColor: {
		                    linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1 },
		                    stops: [
		                        [0, '#FFF'],
		                        [1, '#333']
		                    ]
		                },
		                borderWidth: 0,
		                outerRadius: '109%'
		            }, {
		                backgroundColor: {
		                    linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1 },
		                    stops: [
		                        [0, '#333'],
		                        [1, '#FFF']
		                    ]
		                },
		                borderWidth: 1,
		                outerRadius: '107%'
		            }, {
		                // default background
		            }, {
		                backgroundColor: '#DDD',
		                borderWidth: 0,
		                outerRadius: '105%',
		                innerRadius: '103%'
		            }]
		        },

		        // the value axis
		        yAxis: {
		            min: 0,
		            max: 100,

		            minorTickInterval: 'auto',
		            minorTickWidth: 1,
		            minorTickLength: 10,
		            minorTickPosition: 'inside',
		            minorTickColor: '#666',

		            tickPixelInterval: 30,
		            tickWidth: 2,
		            tickPosition: 'inside',
		            tickLength: 10,
		            tickColor: '#666',
		            labels: {
		                step: 2,
		                rotation: 'auto'
		            },
		            title: {
		                text: 'km/h'
		            },
		            plotBands: $scope.gaugewise.plotBand
		        },

		        series: [{
		            name: 'Speed',
		            data: [80],
		            tooltip: {
		                valueSuffix: ' km/h'
		            }
		        }]

		    },
           // Add some life
		    function (chart) {
		        if (!chart.renderer.forExport) {
		            setInterval(function () {
		                var point = chart.series[0].points[0],
		                    newVal,
		                    inc = Math.round((Math.random() - 0.5) * 20);

		                newVal = point.y + inc;
		                if (newVal < 0 || newVal > 200) {
		                    newVal = point.y - inc;
		                }

		                point.update(newVal);

		            }, 3000);
		        }
		    });
		};
		$scope.loadScoreWiseGraph = function(){
			var self = this;
		   	//console.log(this.get('dateWiseGraph'));
		    var chartHigh = new Highcharts.Chart({
				chart: {
            		renderTo: 'container_scorevote',
			        defaultSeriesType: 'bar',
			        type: 'bar'
		        },
		        title: {
		            text: ''//Customer Score
		        },
		        subtitle: {
		            text: ''
		        },
		        legend: {
		            enabled: false,
		           // align: 'right',
		           // verticalAlign: 'middle'
		        },
		        credits: {
		            enabled: false
		        },
		        tooltip: {
		           // enabled: false,
		            formatter: function() {
                        return 'Score :' + this.x +' Customers :'+ this.y ;
                	}
		        },
		        xAxis: {
		            categories: [{ name : 'Detractors', categories: ['0', '1', '2', '3', '4', '5', '6']}
		            			,{ name : 'Passive', categories: [ '7', '8']}
		            			,{ name : 'Promoter', categories: [ '9', '10']}
		            			],
        			/*labels: {
					    formatter: function () {
						    var text = this.value,
							    formatted = text.length > 25 ? text.substring(0, 25) + '...' : text;

	                        return '<div class="js-ellipse" style="width:30px; overflow:hidden" title="' + text + '">' + formatted + '</div>';
					    },
					    style: {
						    width: '30px'
					    },
					    useHTML: true
				}*/
		            crosshair: true
		        },
		        yAxis: {
		            min: 0,
		            title: {
		                text: ''
		            },
		            interval:1
		        },
		       /* tooltip: {
		            headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
		            pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
		                '<td style="padding:0"><b>{point.y:.1f} mm</b></td></tr>',
		            footerFormat: '</table>',
		            shared: true,
		            useHTML: true
		        },*/
		        plotOptions: {
		            series: {
		                pointWidth: 20,
		                pointPadding: 0,
		                groupPadding: 0
		            }
		        },
		        series: [$scope.scorewise]
		    });
		};
		$scope.loadDateWiseGraph = function(){
				var self = this;
		    	//console.log(this.get('dateWiseGraph'));
		    	var dailySiebeldates = $scope.datewise;
		    	$.each(dailySiebeldates, function(key, val) {
					$.each(val['data'], function(key1, val1) {	
							var date = val1[0];
							var count = parseInt(val1[1]);
							var dValue = date.split('-');
							var y = dValue[0];
							var m = parseInt(dValue[1])-1;
							var d = dValue[2];
							val1[0]=Date.UTC(y, m, d, 0, 0, 0);
							val1[1]=count;
						//}
					});
				});

				var chart = new Highcharts.StockChart({
					chart: {
						 backgroundColor: '#f5f5f5',
						alignTicks: false,
						events: {
							load: function (e) {
								
								  var now = new Date();
								  var date_now=(now.getMonth()) + '/' + (now.getDate()) + '/' + now.getFullYear()  ;
								//alert(now);
								  var myDate=date_now.split('/');
								  var old_year=myDate[2]-1;
								  
								  //var cur_mon=myDate[0]-1;
								  //this.xAxis[0].setExtremes(Date.UTC(old_year, myDate[1],myDate[0]), Date.UTC(myDate[2],myDate[0],myDate[1]));
							}
						},
						ignoreHiddenSeries: true,
						renderTo: $('#container_timeline')[0]
					},
					colors: [ "#000000",'#cd0200', '#d47500',	'#3cb521' ],
					credits: {
						enabled: false
					},
					legend: {
						enabled: true,
						shadow: true
					},
					rangeSelector: {
						   buttons: [{
								type: 'month',
								count: 1,
								text: '1m'
							}, {
								type: 'month',
								count: 2,
								text: '2m'
							},
							{
								type: 'all',
								text: 'All'
							}/*, {
								type: 'year',
								count: 1,
								text: '1y'
							}, {
								type: 'all',
								text: 'All'
							}*/],

					},							   
					navigator: {
						height: 20,
						xAxis: {
							gridLineWidth: 1
						},
						series: {
							type: 'column'
						}
					},
					tooltip: {
						pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b> ({point.percentage:.0f}%)<br/>',
						shared: true
					},
					plotOptions: {
						column: {
							stacking: 'percent'
						},
						series: {
							showInLegend: true,
							//stacking: 'percent',
							dataGrouping: {
								enabled: true,
								forced: true,
								units: [ [ 'day', [1] ]]
							},
							cursor: 'pointer',
							point: {
								events: {
									click: function () {
										//console.log(event.point.series.userOptions.name);
									//	typsy = event.point.series.userOptions.name;
										//jDdate = new Date(this.category);
									//	njDate = jDdate.getMonth()+1+'/'+ jDdate.getDate()+'/'+ jDdate.getFullYear()
										//console.log(njDate);
									//	$('#nameOfGraphTableModal').html(typsy);
									//	var vlu ={style:'datestat', route:'', type:typsy, from_date:njDate, to_date:njDate};
									//	console.log(vlu);
									//	self.set('modelDataTableLoadingValue',vlu);//loadStatckedGraphTable(vlu);

										
										
									}
								}
							}
						}
					},
					 
					xAxis: {
						ordinal: false,
					},
					
					 yAxis: {
					 	opposite: false,
						title: {
							text: 'NPS'
						},
						labels: {
	                		align: 'left',
	             		},

					},
				
					series: dailySiebeldates
				});
		};
		$scope.loadTeamLeadGraph = function(series){
		 		var chartHigh = new Highcharts.Chart({
		 			credits: {
						enabled: false
					},
			        chart: {
						renderTo: 'npsDashboardTeamleadScoreGraph',
			            type: 'column'
			        },
			        title: {
			            text: ''
			        },
			        xAxis: {
			            type: 'category'
			        },
			       /* yAxis:{
			        	text: 'NPS Calls'
			        },*/
			        legend: {
			            enabled: true
			        },
			        colors: [ '#cd0200', '#d47500',	'#3cb521',"#000000" ],
			        tooltip: {
						pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b> ({point.percentage:.0f}%)<br/>',
						shared: true
					},
			        plotOptions: {
			        	column: {
							stacking: 'percent'
						},
			            series: {
			                borderWidth: 0,
			                dataLabels: {
			                    enabled: false,
			                    style: {
			                        color: 'white',
			                        textShadow: '0 0 2px black, 0 0 2px black'
			                    }
			                },
			               //stacking: 'percent'
			            }
			        },

			        series: series.main,
			        drilldown: {
			            activeDataLabelStyle: {
			                color: 'white',
			                textShadow: '0 0 2px black, 0 0 2px black'
			            },
			            series: series.drill
			        }
			    });
	 	};
	 	$scope.loadLocationsGraph = function(){
			 	var self = this;
		    	/*var dailySiebelStatus = series;
		    	var completeArr = [], detractor = [], passive = [], permoter = [], scrArr = [], totArr = [], statArr = [];
						
		    	$.each(dailySiebelStatus, function( key, value ){
					 detractor.push(parseInt(value.detractor));
					 passive.push(parseInt(value.passive));
					 totArr.push(parseInt(value.detractor)+parseInt(value.permoter)+parseInt(value.passive));
					 statArr.push(value.cat_name);
					 permoter.push(parseInt(value.permoter));
					
				});
				completeArr[0] = detractor;
				completeArr[1] = passive;
				completeArr[2] = permoter;
				completeArr[3] = statArr;
				completeArr[4] = totArr;
				console.log(completeArr);*/
				//completeArr[5] = scr1Arr;
		   		var chartHigh = new Highcharts.Chart({
					credits: {
						enabled: false
					},
					chart: {
						renderTo: 'stackedChart',
			            defaultSeriesType: 'column',
			         	type: 'column'

					},
					colors: ["#000000", '#cd0200', '#d47500',	'#3cb521' ],
					title: {
						text: '',
					},
					xAxis: {
						min:0,
						max:10,
						categories:$scope.locationwise.locations,// completeArr[3],
						labels: {
							style: {
								width: '100px',
                				fontSize: '13px',
								fontFamily: 'Verdana, sans-serif'
							},
						 	useHTML: true,
						},
					//	tickWidth: 1,
					},
					scrollbar:{
		                enabled:true
		            },
					yAxis: {
						title: {
							text: '%age '
						}
					},
					tooltip: {
						pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b> ({point.percentage:.0f}%)<br/>',
						shared: true
					},
					plotOptions: {
						bar: {
							pointWidth: 60,
		                    pointpadding:0,
		                    groupPadding:0,
		                    dataLabels: {
		                        enabled: true
		                    }
		                },
						column: {
							stacking: 'percent'
						},
						series: {
							cursor: 'pointer',
							point: {
								events: {
									click: function () {
									//	$("#routeStackedModel").modal("show");
										var da='', db='';
										var ftD = $('#reservation').val();
										var ft  = ftD.split('-');
										if(ftD != ''){
											da=ft[0], db=ft[1];
										}

										var ct = this.category.replace(" ","");
										var feedType = event.point.series.userOptions.name;
										$('#nameOfGraphTableModal').html(feedType);
										var vlu ={style:'substat', route:this.category, type:feedType, from_date:da, to_date:db};
										//loadStatckedGraphTable(vlu);
										console.log(vlu);
										self.set('modelDataTableLoadingValue',vlu);
									
									}
								}
							}
						}
						//dataLabels: dataLabaling
					},
			        series: $scope.locationwise.series
			    });
	 	};
/*	$scope.loginErrFlg = false;
	$scope.loginErrMsg = null;
	$scope.logingUser = false;
	$scope.btnGrey = true;
	$scope.btnGreen = false;

	$scope.errorEmailEmpty = true;
	$scope.step_1 = true;
	
	$scope.errorMsgEmail = null;
	$scope.errorEmailEmpty = false;
	$scope.errorEmail = false;
	$scope.email = '';
	
	$scope.applyEvents = function() {
		$('#UserUsername, #UserPassword')
		.keyup(function(e) {
			if (e.keyCode == 13) {
				$scope.$apply($scope.doLogin());
			}
		});
		$('#inputEmail').blur(function() {
			var email = $('#inputEmail').val();
			if (email=="") {
				$scope.errorEmailEmpty = true;
				
			}else{
				$scope.errorEmailEmpty = false;
			} 
		});
	};

	$scope.applyEvents();
	$scope.isFormValid = function() {
		return true;
	};

	$scope.doLoginData = null;
	$scope.doLogin = function() {
		if ($scope.logingUser) {
			return;
		}
		if (!$scope.isFormValid()) {
			return;
		}
		var postData = $('#UserLoginForm').serialize();
		$scope.logingUser = true;
		AppCore.loader.show({text: 'Loading'});
		SvcLogin.save(
			AppCore.parseNGAjaxReq({}),
			AppCore.serializeReqData(postData),
			function(response) {
//				console.log(response); return;
				$scope.loginErrFlg = false;
				AppCore.loader.hide();
				AppCore.webService.response = response;
				if (AppCore.webService.isResponseSuccess()) {
					$scope.doLoginData = response.data.data;
					$scope.doLoginParseData();
				} else {
					$scope.logingUser = false;
					var error_desc = response.data.description;
					$scope.loginErrFlg = true;
					$scope.loginErrMsg = error_desc;
				}
			}
		);
	};
	$scope.doLoginParseData = function() {
		if (typeof $scope.doLoginData.secret_question_undefined !== 'undefined' && $scope.doLoginData.secret_question_undefined) {
			$scope.logingUser = false;
			//$("#securityQAModal").modal();
			AppCore.redirect($scope.doLoginData.next_url);
		} else {
			AppCore.redirect($scope.doLoginData.next_url);
		}
	};
	$scope.securityQACancel = function() {
		AppCore.redirect($scope.doLoginData.next_url);
	};
	$scope.securityQASubmit = function() {
		AppCore.redirect($scope.doLoginData.secret_question_url);
	};

	$scope.validateForgetPassWord = function() {

		$scope.errorEmailEmpty = false;
		$scope.errorEmail = false;
		var reg = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
		if ($scope.email == ''){
			$scope.errorEmailEmpty = true;
			$scope.errorEmail = true;
			$scope.btnGreen = false;	
			$scope.btnGrey = true;
			$scope.errorMsgEmail = "Please provide email address";
			return false;
		}else if (reg.test($scope.email) == false){
			$scope.errorEmailEmpty = true;
			$scope.errorEmail = true;
			$scope.btnGrey = true;
			$scope.btnGreen = false;	
			$scope.errorMsgEmail = "Invalid email address";
			return false;
		}else{
			$scope.btnGrey = false;
			$scope.btnGreen = true;	
			return true;
		}
	}
	
	$scope.forgetPassWord = function() {		
	
		if ($scope.validateForgetPassWord() == false){
			return false;
		}
		var postData = $('#UserForgotPasswordForm').serialize();
		AppCore.loader.show({text: 'Loading'});
		SvcForgotPassword.save(
			AppCore.parseNGAjaxReq({}),
			AppCore.serializeReqData(postData),
			function(response) {
				AppCore.loader.hide();
				if (response.data.success_status == 1) {
					$("#forgotPanel").html($("#forgetSuccessMsg").html());
				} else {
					$scope.errorEmailEmpty = true;
					$scope.errorEmail = true;
					$scope.errorMsgEmail = response.data.description;
				}
			}
		);
	};*/
	}
]);