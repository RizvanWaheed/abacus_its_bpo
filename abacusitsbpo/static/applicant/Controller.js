ApplicantModule.controller('ApplicantController', ['$scope', '$location', '$upload', '$filter', 'ApplicantServices',
    function ($scope, $location, $upload, $filter, SetupServices) {

        //$scope.setLoadingTemplate(false);
        $scope.contentsLoaded = false;
        $scope.PageData = {};
        $scope.date = currDate;
        $scope.selectDate = currDate;
        $scope.format = 'yyyy-MM-dd';

        //console.log(designations);
        //console.log(departments);
        //console.log(cities);
        //console.log(projects);
        //console.log(educations);
        //console.log(institutes);

        $scope.listOfSources = [{
            name: 'Facebook'
        }, {
            name: 'Rozee'
        }, {
            name: 'Linkdin'
        }, {
            name: 'Job Fair'
        }, {
            name: 'University'
        }, {
            name: 'Refrence'
        }, {
            name: 'Others'
        }];

        $scope.listOfMaritalStatus = [{
            name: 'Single'
        }, {
            name: 'Engaged'
        }, {
            name: 'Married'
        }, {
            name: 'Divorced'
        // }, {
        //     name: 'Saperated'
        // }, {
        //     name: 'Complicated'
        }];

        // console.log(cities);
        // console.log($.parseJSON(cities));
        // console.log(JSON.parse(cities));
        // console.log(angular.fromJson(cities));
        // cities
        $scope.listOfCities = cities;
        $scope.listOfEducations = educations;
        $scope.listOfInstitutes = institutes;
        $scope.listOfMajors = majors;
        $scope.listOfLanguages = languages;

        // $scope.listOfCities = angular.fromJson(cities);
        $scope.listOfDepartments = {};
        $scope.listOfDesignations = {};
        $scope.listOfJobCategory = {};
        $scope.listOfOrintations = {};
        $scope.watchInstitute = {
            id: 0,
            name: ''
        };

        $scope.years = [];
        var d = new Date();
        var n = d.getFullYear();
        $scope.years.push({
            id: 1111,
            name: 'Continue...'
        });
        for (var i = 0; i < 70; i++) {
            $scope.years.push({
                id: n - i,
                name: n - i
            });
        }

        $scope.showCompany = false;

        $scope.scoreModel = [];
        $scope.searchNumber = '';

        $scope.npsCall = [];
        $scope.npsCallGroup = [];

        $scope.selectedGender = 0;
        $scope.selectedCS = 2;
        $scope.sortObj = {
            sortby: 'name',
            sortdr: 'Asc'
        };
        $scope.page = 1;
        $scope.PagingHeaders = {};

        //$scope.setPageNameData('Recruitment');
        $scope.paramsRecruitments = {
            action: 'getRecruitmentData.json',
            company_id: $scope.selectedCompanyID,
        };
        $scope.dateOptions = {
            //    dateDisabled: disabled,
            formatYear: 'yyyy',
            maxDate: new Date(),
            minDate: new Date(1960, 1, 1),
            startingDay: 1
        };
        $scope.alerts = [];

        function disabled(data) {
            var date = data.date,
                mode = data.mode;
            return mode === 'day' && (date.getDay() === 0 || date.getDay() === 6);
        }
        $scope.open = function () {
            $scope.popup.opened = true;
        };
        $scope.open1 = function () {
            $scope.popup.opened1 = true;
        };
        $scope.openStart = function (key) {
            ///console.log(key)
            $scope.popup.openedStart[key] = {
                opened: true
            };
        };
        $scope.openEnd = function (key) {
            /// console.log(key)
            $scope.popup.openedEnd[key] = {
                opened: true
            };
        };
        $scope.setDate = function (year, month, day) {
            $scope.applicant.dob = new Date(year, month, day);
        };
        $scope.setCnicIssurenceDate = function (year, month, day) {
            $scope.applicant.cnic_insurance_date = new Date(year, month, day);
        };
        $scope.popup = {
            opened: false,
            openedStart: [],
            openedEnd: []
        };
        $scope.addAlert = function (type, message, time) {
            //console.log(type);
            //console.log(message);
            //console.log(time);
            $scope.alerts.push({
                type: type,
                message: message,
                time: time
            });
            // console.log($scope.alerts);
        };

        $scope.closeAlert = function (index) {
            $scope.alerts.splice(index, 1);
        };

        $scope.setFormDefault = function () {
            //$scope.alerts = [];cnic_insurance_date
            $scope.existing_employee = false;
            $scope.applicant = {
                id: '',
                cnic: '1111111111111',
                first_name: '',
                last_name: '',
                father_name: '',
                contact: '',
                eaddress: '',
                gender: 'Male',
                dob: new Date(1985, 05, 28),
                cnic_insurance_date: new Date(1985, 05, 28),
                city_id: '',
                language_id: '',
                address: '',
                state: 'applicant',
                marital_status:'Single',
                comments: '',
                source: '',
                imageText:'',
                applicant_educations: [],
                applicant_refers: [],
                applicant_experiences: [],
                applicant_typing: [],
            };
            $scope.education = {
                education_id: 0,
                year: 0,
                institute: '',
                institute_id: 0,
                major_id: 0,
                others: ''
            };

        };

        $scope.setFormDefault();
        // $scope.$watch('applicant.cnic', function (newValue,oldValue, scope) {
        //     console.log(oldValue+"   "+newValue);
        //     var regex = new RegExp('^[0-9]{5}-[0-9]{7}-[0-9]{2}$');
        //
        //     // if(typeof newValue !== 'undefined') {
        //         var len = newValue.length;
        //         if (len == 5 | len == 13) {
        //             $scope.applicant.cnic = newValue + "-";
        //         }
        //         // if (regex.test($scope.applicant.cnic)) {
        //         //     console.log("matches");
        //         //     $scope.isMatch = "Regex match!";
        //         // } else {
        //         //     $scope.isMatch = "Regex mismatch!";
        //         // }
        //     // }
        //     // if (newValue!=oldValue) Data.setFirstName(newValue);
        // });

        // $scope.cnicChanges = function() {
        //     var regex = new RegExp('^[0-9]{5}-[0-9]{7}-[0-9]{2}$');
        //     console.log($scope.applicant.cnic)
        //     if(typeof $scope.applicant.cnic !== 'undefined') {
        //
        //
        //         var len = $scope.applicant.cnic.length;
        //         if (len == 5 | len == 13) {
        //             $scope.applicant.cnic += "-";
        //         }
        //         if (regex.test($scope.applicant.cnic)) {
        //             console.log("matches");
        //             $scope.isMatch = "Regex match!";
        //         } else {
        //             $scope.isMatch = "Regex mismatch!";
        //         }
        //     }
        //
        // }
        // $scope.initializedApplicantCnic = '35202-3037622-5';
        $scope.allEdu = []; //{};
        $scope.allExperience = []; //{};
        $scope.selectedItem = "";
        $scope.forwordHide = true;
        $scope.updateselectedItem = function () {
            //alert($scope.selectedItem);
            if ($scope.selectedItem == 'Forward') {
                $scope.forwordHide = false;
            } else {
                $scope.forwordHide = true;
            }
        }
        /*$scope.updateselectedItem = function(){
        	$scope.allEdu.push({ education_id:0, year:0, institute:'' });
        }*/
        $scope.addEducation = function () {
            $scope.applicant.applicant_educations.push({
                education_id: 0,
                year: 2018,
                institute: '',
                institute_id: '',
                major_id: '',
                status: false,
                others: ''
            });
            // $('select').select2({
            //     theme: "bootstrap",
            //     height: 'resolve' // need to override the changed default
            // });
        }
        $scope.addRefrence = function () {
            $scope.applicant.applicant_refers.push({
                name: '',
                phone: '',
                education_id: 0,
                // data: {
                //     'opened': false
                // }
            });
            // $('select').select2({
            //     theme: "bootstrap",
            //     height: 'resolve' // need to override the changed default
            // });
        }
        $scope.removeRefrence = function (key) {
            //var index = $scope.allEdu.indexOf(key);
            //if (index > -1) {
            $scope.applicant.applicant_refers.splice(key, 1);
            //}
        }
        $scope.removeEducation = function (key) {
            //var index = $scope.allEdu.indexOf(key);
            //if (index > -1) {
            $scope.applicant.applicant_educations.splice(key, 1);
            //}
        }
        $scope.addExperience = function () {
            $scope.applicant.applicant_experiences.push({
                company_name: '',
                designation: '',
                job_description: '',
                started: '',
                ended: ''
            });
        }
        $scope.removeExperience = function (key) {
            //var index = $scope.allEdu.indexOf(key);
            //if (index > -1) {
            $scope.applicant.applicant_experiences.splice(key, 1);
            //}
        }
        $scope.getPageData = function (params) {
            //DashboardHelper.showLoader();
            SetupServices.get(
                AppCore.parseNGAjaxReq(params),
                function (response) {
                    if (response.data.success_status) {
                        $scope.parseRecruitmentData(response);
                        $("#dob").inputmask({
                            "mask": "9999-99-99"
                        });
                        DashboardHelper.hideLoader();

                    } else {
                        DashboardHelper.hideLoader();
                        //$scope.passwordMessage = response.data.description;
                    }
                },
                function (error) {
                    console.log(error);
                    return false;
                }
            );
        };
        $scope.parseRecruitmentData = function (response) {


            //$scope.listOfCities = angular.copy(response.data.cities);
            //$scope.listOfDepartments  = angular.copy(response.data.department);
            //$scope.listOfDesignations = angular.copy(response.data.designations);
            //$scope.listOfJobCategory = angular.copy(response.data.job_category);
            //$scope.listOfEducations = angular.copy(response.data.educations);
            //$scope.listOfInstitutes = angular.copy(response.data.institutes);
            //$scope.listOfOrintations = angular.copy(response.data.orintations);
            //$scope.applicant.applicant_orientations = angular.copy(response.data.orintations);
            console.log(response);

            // $('select').select2({
            //     theme: "bootstrap",
            //     height: 'resolve' // need to override the changed default
            // });
            return false;
            /*console.log($scope.companies[0].categories_levels);

            $scope.callStatus	= angular.copy(response.data.call_status);
            $scope.categories	= angular.copy(response.data.categories);
            $scope.categories_levels = $scope.companies[0].categories_levels;
            $scope.affinityList = [];
            for(var i = 1; i<= $scope.categories_levels; i++){
            	console.log(i);
            	$scope.affinityList.push({
            		headLine   : 'Affinity Level '+i,
            		categoryID : 'AffinityID'+i,
            		categoryLevel : i,
            		categoryData : [],
            	});
            }


            $scope.parseSelectedAffinityData(0, 0);

            $scope.gender	 	= angular.copy(response.data.gender);
            $scope.selectedCategory = [$scope.categories[0]];*/

        };
        $scope.parseSelectedAffinityData = function (level, category_id) {
            console.log(level);
            console.log($scope.categories_levels);
            //return false;
            if ($scope.categories_levels == level) {
                $scope.selectedCategory = category_id;
                return true;
            }
            var newLevel = level + 1;
            $scope.affinityList[level].categoryData = [];
            angular.forEach($scope.categories, function (value, key) {
                if (value.level == newLevel && value.category_id == category_id) {
                    $scope.affinityList[level].categoryData.push($scope.categories[key]);
                }

            });
            //console.log($scope.affinityList[0].categoryData);
        }
        //$scope.getPageData($scope.paramsRecruitments);
        //$scope.selectedCategory = [$scope.categories[0]];
        $scope.ValidatePhone = function (e) {
            var charCode = (e.which) ? e.which : e.keyCode;
            // Allow: backspace, delete, tab, escape, enter and .
            if ($.inArray(charCode, [46, 8, 9, 27, 13, 110, 190]) !== -1 ||
                // Allow: Ctrl+A, Command+A
                (charCode == 65 && (e.ctrlKey === true || e.metaKey === true)) ||
                // Allow: home, end, left, right, down, up
                (charCode >= 35 && charCode <= 40)) {
                // let it happen, don't do anything
                return;
            }
            var len = $scope.searchNumber.trim().toString().length;
            // Ensure that it is a number and stop the keypress
            if (len > 10 || (e.shiftKey || (charCode < 48 || charCode > 57))) {
                e.preventDefault();
            }

        }
        $scope.searchApplicantCnic = function () {
            //console.log($scope.searchNumber);
            //console.log($scope.applicantForm.cnic.$invalid);
            if ($scope.existing_employee) return;
            if ($scope.applicantForm.cnic.$invalid) {
                var cnicNumber = $scope.applicant.cnic;
                $scope.setFormDefault();
                $scope.applicant.cnic = cnicNumber;
                return;
            }
            DashboardHelper.showLoader();
            //var cnic = $scope.applicant.cnic.trim();
            var params = {
                action: 'search_applicant.json',
                cnicNumber: $scope.applicant.cnic,
                company_id: $scope.selectedCompanyID,
            };
            // SetupServices.post(
            //     AppCore.parseNGAjaxReq(params),
            //     function (response) {
            //         //console.log(response);
            //         if (response.data.success_status) {
            //             $scope.parseCnicData(response.data);
            //         } else {
            //             //$scope.setFormDefault();
            //             DashboardHelper.hideLoader();
            //             $scope.applicant.cnic = params.cnicNumber;
            //         }
            //     },
            //     function (error) {
            //         console.log(error);
            //     }
            // );
            SetupServices.save(
				AppCore.parseNGAjaxReq({action: 'search_applicant'}),
			    JSON.stringify({cnicNumber: $scope.applicant.cnic}),
				function (response) {
                    console.log(response);
                    if (response.success_status) {
                        $scope.parseCnicData(response);
                    } else {
                        //$scope.setFormDefault();
                        DashboardHelper.hideLoader();
                        $scope.applicant.cnic = params.cnicNumber;
                    }
                },
                function (error) {
                    console.log(error);
                }
			);

        };
        $scope.parseCnicData = function (data) {
            console.log(data);
            // return;
            DashboardHelper.hideLoader();

            if (data.status == 500) {
                alert('sign In again');
                $window.location.href = 'http://localhost:8642/abs';
                return;
            }
            /*if(data.success_status == false){

            	$scope.setFormDefault();
            }else{*/
            /*$scope.applicant = {
				id: data.applicant.id,
				cnic: data.applicant.cnic,
				first_name: data.applicant.first_name,
				contact: data.applicant.contact,
				eaddress: data.applicant.eaddress,
				gender: data.applicant.gender,
				city_id: data.applicant.city_id,
				address: data.applicant.address,
				applicant_educations: data.applicant.applicant_educations,
				applicant_experiences: data.applicant.applicant_experiences,
            };*/

            console.log(data.applicant)
            $scope.existing_employee = true;
            $scope.applicant = angular.copy(data.applicant);
            if (!angular.equals([], $scope.applicant.applicant_comments)) {
                $scope.applicant.comments = $scope.applicant.applicant_comments[0].remarks;
            }

            var dt = data.applicant.dob.split('T');
            var dt2 = dt[0].split('-');
            $scope.setDate(dt2[0], dt2[1] - 1, dt2[2]);
            // cnic_insurance_date
            if(data.applicant.cnic_insurance_date){
                var cid = data.applicant.cnic_insurance_date.split('T');
                var cid2 = cid[0].split('-');
                $scope.setCnicIssurenceDate(cid2[0], cid2[1] - 1, cid2[2]);
            }



            if (data.applicant.state == "applicant") {
                $scope.addAlert('', 'Applicant is in process HR will contact you.', '5000');
            }

            angular.forEach($scope.applicant.applicant_educations, function (value, key) {
                //console.log(value);
                //console.log(key);

                $scope.applicant.applicant_educations[key].others = {
                    id: value.institute_id,
                    name: value.institut
                };
            });
            $scope.applicant.state += ' On Date: ' + $scope.applicant.modified;
            console.log($scope.applicant);

        };
        $scope.saveEmployeeInformation = function (whattodo) {
            if ($scope.existing_employee) return;
            if (!$scope.applicantForm.$valid) {
                return false;
            }
            //console.log($scope.applicant.applicant_educations);
            // formatDate(new Date(deadlineDate.getTime() + deadlineDate.getTimezoneOffset() * 60000));
            $scope.applicant.cnic_insurance_date = moment($scope.applicant.cnic_insurance_date).format('yyyy-MM-DD');
            $scope.applicant.dob = moment($scope.applicant.dob).format('yyyy-MM-DD');
            angular.forEach($scope.applicant.applicant_educations, function (value, key) {
                //console.log(value);
                //console.log(key);
                var insti = value.others;
                $scope.applicant.applicant_educations[key].institute_id = insti.id;
                $scope.applicant.applicant_educations[key].institute = insti.name;
                // if(value.level == newLevel && value.category_id == category_id){
                // 	    $scope.affinityList[level].categoryData.push($scope.categories[key]);
                // }
            });
            angular.forEach($scope.applicant.applicant_experiences, function (value, key) {
                $scope.applicant.applicant_experiences[key].started = moment(value.started).format('yyyy-MM-DD');
                $scope.applicant.applicant_experiences[key].ended = moment(value.ended).format('yyyy-MM-DD');
            });
            //console.log($scope.applicant.applicant_educations);
            //return false;

            DashboardHelper.showLoader();
            SetupServices.save(
                AppCore.parseNGAjaxReq({
                    action: 'save_applicant'
                }),
                // headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8;application/json'},
                JSON.stringify($scope.applicant),
                function (response) {
                    $scope.processSaveResponse(response);
                },
                function (error) {
                    $scope.processSaveResponse(error.data);
                }
            );

        };
        $scope.processSaveResponse = function (response) {
            if (response.success_status) {
                DashboardHelper.hideLoader();
                $scope.addAlert('success', 'Applicant information saved successfully.', '5000');
                $scope.setFormDefault();
                //$scope.closeUserModel();
                //$scope.getPageData();

            } else {
                $scope.addAlert('error', 'Applicant information not saved.', '5000');
                DashboardHelper.hideLoader();
                //$scope.passwordMessage = response.data.description;
            }

        };
        $scope.closeUserModel = function () {
            $('#userAddModal').modal('hide');
        };
        $scope.openUserModel = function (key) {


            if (key != '' || key == '0') {
                keyVal = parseInt(key);
                //console.log($scope.users[keyVal].user_id);
                $scope.updateUsersVal = $scope.users[keyVal]; //angular.copy();
                $scope.updateUsr = true;
                $scope.modelName = "Update User";
                $scope.selectedRole = $scope.updateUsersVal.role_id;
                $scope.showUserReportingTo(keyVal);
                $scope.selectedReporting = $scope.users[keyVal].user_id;
            } else {
                $scope.updateUsr = false;
                $scope.modelName = "Add User";
                $scope.selectedRole = 0;
                $scope.updateUsersVal = {
                    id: 0,
                    username: '',
                    password: '',
                }
                //	$scope.selectedRole = "";
                $scope.selectedReporting = 0;
            }
            //console.log($scope.updateUsersVal);
            $('#userAddModal').modal();
        };

        //  $scope.$watch('watchInstitute', function(newValue, oldValue) {
        //     scope.counter = scope.counter + 1;
        //     scope.lastvalue = oldValue;
        //     scope.currentvalue = newValue;
        //  });
        $scope.onSelectCallback = function (item, model) {
            console.log(item);
            console.log(model);
            //  $scope.counter++;
            //     $scope.eventResult = {item: item, model: model};
        };
        //
        $scope.refreshResults = function ($select) {
            var search = $select.search,
                list = angular.copy($select.items),
                FLAG = -1;
            //remove last user input
            list = list.filter(function (item) {
                return item.id !== FLAG;
            });

            if (!search) {
                //use the predefined list
                $select.items = list;
            } else {
                //manually add user input and set selection
                var userInputItem = {
                    id: FLAG,
                    name: search
                };
                $select.items = [userInputItem].concat(list);
                $select.selected = userInputItem;
            }
        };

    }
]);
