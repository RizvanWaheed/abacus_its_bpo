dashboardControllers.controller('ReportsCtrl', ['$scope', '$timeout','$routeParams','$location', '$upload', 'SvcDashboard',
	function($scope,$timeout,$routeParams,$location,$upload,SvcDashboard){
		
		$scope.contentsLoaded = false;
		$scope.PageData 	 = {};
		$scope.date 		 = currDate;
		$scope.selectDate    = currDate;
		$scope.format 		 = 'yyyy-MM-dd';
	//	console.log('I am in reports controller');
		$scope.roleIDGlobal   = userRoleID;
		$scope.companyIDGlobal= userCompanyID; 
		$scope.myRoleN		  = userRole;

		$scope.selectedCompanyID     = userCompanyID;
		$scope.selectedCompanyName   = userCompany;
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
	
		$scope.getReportData = function(){
			//to send services to get Access of inner pages and companies
			params = {
				action: 'getActivities.json',
				company_id:$scope.selectedCompanyID
			};
			SvcDashboard.get(
				AppCore.parseNGAjaxReq(params),
				function(response) {		
					if (response.data.success_status){
						$scope.parseActivityPageData(response);
					}else{
						$scope.parseActivityPageData(response);
					}
				},
				function(error) {
					console.log(error);
					return false;
				}
			);
		};
		$scope.parseActivityPageData = function(response){
			$scope.menu	     = angular.copy(response.data.menu);
			$scope.companies = angular.copy(response.data.companies);		
		};
		$scope.viewCompany = function(company_id){

			$scope.selectedCompanyID     = company_id;
		//    $scope.selectedCompanyName   = userCompany;
		    angular.forEach($scope.companies, function(value, key) {
				if(value.id == company_id)
					$scope.selectedCompanyName = value.name;
			});
			$scope.currentChild.selectedCompanyID = company_id;
			$scope.params.company_id = company_id;
			$scope.getPageData($scope.params, $scope.currentChild);
		};
		//if($scope.companyIDGlobal == 1){
		$scope.getReportData();
	
	/*,	hash: $routeParams.hash,*/
		$scope.defSection = templatePath+'/tpl_rptactivities';
		DashboardHelper.showLoader();
		var objSrch = $location.search();
		$scope.section = typeof objSrch.section !== 'undefined' && objSrch.section ? objSrch.section : $scope.defSection;
		$scope.view_by = $scope.section;
		
		$scope.viewByChg = function() {
			$scope.showSection($scope.view_by);
		};
		$scope.viewByClick = function(page) {
			DashboardHelper.showLoader();
			$scope.view_by = page;
			$scope.showSection($scope.view_by);
		};
		
		$scope.templates = {
			rptactivities_group: {
				url: templatePath+'/tpl_rptactivities'
			},
			rpttrends_group: {
				url: templatePath+'/tpl_rpttrends'
			},
			rptscores_group: {
				url: templatePath+'/tpl_rpttrendsagent'
			}
		};
		$scope.setLoadingTemplate = function(loading) {
			$scope.loadingTemplate = loading;
		};
		$scope.setTemplate = function(setLoadingTemplate) {
			if (setLoadingTemplate) {
				$scope.setLoadingTemplate(true);
			}
			$scope.template = typeof $scope.templates[$scope.section] !== 'undefined' ? $scope.templates[$scope.section] : $scope.templates[$scope.defSection];
		
		};
		$scope.showSection = function(section) {
			$location.search('');
			if (typeof section === 'string') {
				$location.search('section', section);
			} else if (typeof section === 'object') {
				$location.search(section);
			}
		};
		$scope.setTemplate(true);
		$scope.isSection = function(section) {
			if ($scope.section == section) {
				return true;
			} else {
				return false;
			}
		};
		$scope.$on("$routeUpdate", function(event, route) {
	    	// some code here
			var objSrch = $location.search();
			$scope.section = typeof objSrch.section !== 'undefined' && objSrch.section ? objSrch.section : $scope.defSection;
			$scope.setTemplate();
		});

		$scope.setPageNameData = function(a){
			$scope.pageName = a;
		}
		$scope.setPageHeader = function(name){
			$scope.pageName = name;
		};
		$scope.setPageValue = function(from,to,total){
			$scope.pageFrom = from;
			$scope.pageTo   = to;
			$scope.pageTotal= total;
		};

		$scope.pagination = function(headers){
			//console.log(headers);
			$scope.PagingHeaders = headers;
			AppCore.paging.init();
			AppCore.paging.totalPages = $scope.PagingHeaders.total_pages;
			AppCore.paging.currPage   = $scope.PagingHeaders.page_number;
			$scope.PagingHeaders.pagingArr = [];
			if (AppCore.paging.totalPages > 1) {
				var objPaging = AppCore.paging.getStartEndLoop();
				for (var pLoop = objPaging.LinksStart; pLoop <= objPaging.LinksEnd; pLoop++) {
					$scope.PagingHeaders.pagingArr.push({pNum: pLoop, isActive: (pLoop == AppCore.paging.currPage)});
				}
			}
			$scope.setPageValue($scope.PagingHeaders.showing_from, $scope.PagingHeaders.showing_to, $scope.PagingHeaders.total);
		};

		$scope.showPage = function(page) {
			if (page == 'prv') {
				if ($scope.page <= 1) return false;
				$scope.page = $scope.page - 1;
			} else if (page == 'nxt') {
				if ($scope.page >= $scope.PagingHeaders.total_pages) return false;
				$scope.page = $scope.page + 1;
			} else {
				page = parseInt(page);
				if (page == $scope.page) return false;
				$scope.page = page;
			}
			//$scope.params.page = $scope.page;
			//console.log($scope.params);
			$scope.getPageData($scope.params);
		};
		$scope.params = '';
		$scope.headers= '';


		$scope.getPageData = function(params, scope) {
			$('html').removeClass('menu-open');
		//DashboardHelper.showLoader();
			//console.log(params);
			$scope.currentChild = scope;
			params.company_id 	= $scope.selectedCompanyID;
			params.page   	  	= $scope.page;
			$scope.params 		= params;
			//$scope.params.sortby= $scope.sortObj.sortby;
			//$scope.params.sortdr= $scope.sortObj.sortdr;
			$scope.params.page  = $scope.page;

			SvcDashboard.get(
				AppCore.parseNGAjaxReq(params),
				function(response) {
					if (response.data.success_status){
						$scope.parsePageData(response);
						DashboardHelper.hideLoader();
					}else{
						DashboardHelper.hideLoader();	
					}
				},
				function(error) {
					console.log(error);
					return false;
				}
			);
		};
		$scope.parsePageData = function(response) {

			if($scope.params.action == 'getActivitiesReports.json'){
				$scope.parseReportActivitiesData(response);
			}else if($scope.params.action == 'getDateTrandsReports.json'){
				$scope.parseReportDateTrandsData(response);
			}else if($scope.params.action == 'getAssignedCustomers.json'){
				$scope.parseAssignedCustomersData(response);
			}
			
		};
		
		$scope.parseReportActivitiesData = function(response){
			$scope.activitiesRpt  = angular.copy(response.data.activities);
			$scope.headers	        = angular.copy(response.data.headers);
	
			$scope.showPagination = true;	
			var headers = $scope.headers;
			$scope.pagination(headers);
		};
		$scope.parseReportDateTrandsData = function(response){
			//console.log(response);
			$scope.activitiesRpt  = angular.copy(response.data.activities);
			$scope.headers	      = angular.copy(response.data.headers);
			//console.log($scope.headers);	
			$scope.showPagination = true;	
			var headers = $scope.headers;
			$scope.pagination(headers);
		};
	}
]);