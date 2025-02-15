# BRANCH MODEL

     # last migration in 'MASTER' branch  '0013_branch_dst_time.py' 
     # last migration in 'SANDBOX' branch "0015_branch_is_pre_approval_required_and_more.py" (Ak-hr-service)

     ### REMOVED_FIELDS: is_delete

     ### ADDED_FIELD: deleted_by, is_pre_approval_required, pre_approval_by

     ### CHANGES:

            ### 0014_remove_branch_is_delete_branch_deleted_by.py
             
            operations = [
                    migrations.RemoveField(
                        model_name='branch',
                        name='is_delete',
                    ),
                    
                   migrations.AddField(
                        model_name='branch',
                        name='deleted_by'
                        field=models.UUIDField(null=True),
                    ),
                ]


             ### 0015_branch_is_pre_approval_required_and_more.py
                  
            operations = [
                           migrations.AddField(
                        
                                 model_name='branch',
                                name='is_pre_approval_required',
                                 field=models.BooleanField(default=False, null=True),
                             ),

                           migrations.AddField(
                                 model_name='branch',
                                name='pre_approval_by',
                                 field=models.CharField(default='TEAM_LEADER', null=True),
                             ),
                         ]
    
   
            

#### COMPANY MODEL
    # last migration in 'MASTER' branch  '0004_alter_company_is_delete.py' 
     # last migration in 'SANDBOX' branch "0005_remove_company_is_delete_company_deleted_by.py" (Ak-hr-service)

     ### REMOVED_FIELDS: is_delete

     ### ADDED_FIELD: deleted_by

     

     ### CHANGES:
                # 0005_remove_company_is_delete_company_deleted_by.py
                

                operations = [
                            migrations.RemoveField(
                                model_name='company',
                                name='is_delete',
                            ),
                            migrations.AddField(
                                model_name='company',
                                name='deleted_by',
                                field=models.UUIDField(null=True),
                            ),
                        ]


#### DEPARTMENT MODEL 

    # last migration in 'MASTER' branch  '0005_department_updated_by_alter_department_incharge.py' 
    # last migration in 'SANDBOX' branch "0007_remove_department_is_delete_department_deleted_by.py"

    ### REMOVED_FIELDS: is_delete

    ### ADDED_FIELD: deleted_by

    ### MODIFIED_FIELD: branch_uuid, company_uuid,

    ### CHANGES:
        ## 0006_alter_department_branch_uuid_and_more.py

        operations = [
                migrations.AlterField(
                    model_name='department',
                    name='branch_uuid',
                    field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='branch_department', to='branch.branch'),
                ),
                migrations.AlterField(
                    model_name='department',
                    name='company_uuid',
                    field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_department', to='company.company'),
                ),
            ]
            

        ## 0007_remove_department_is_delete_department_deleted_by.py

        operations = [
                    migrations.RemoveField(
                        model_name='department',
                        name='is_delete',
                    ),
                    migrations.AddField(
                        model_name='department',
                        name='deleted_by',
                        field=models.UUIDField(null=True),
                    ),
                ]


    

### DESIGNATION MODEL

    # last migration in 'MASTER' branch  '0005_alter_designation_is_delete.py' 
    # last migration in 'SANDBOX' branch "0007_remove_designation_is_delete_designation_deleted_by.py"

    ### REMOVED_FIELDS: is_delete

    ### ADDED_FIELD: deleted_by

    ### MODIFIED_FIELD: branch_uuid, company_uuid,

    ### CHANGES:
        
        # 0006_alter_designation_branch_uuid_and_more.py
        operations = [
                migrations.AlterField(
                    model_name='designation',
                    name='branch_uuid',
                    field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='branch_designation', to='branch.branch'),
                ),
                migrations.AlterField(
                    model_name='designation',
                    name='company_uuid',
                    field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_designation', to='company.company'),
                ),
            ]

        # 0007_remove_designation_is_delete_designation_deleted_by.py
        operations = [
                migrations.RemoveField(
                    model_name='designation',
                    name='is_delete',
                ),
                migrations.AddField(
                    model_name='designation',
                    name='deleted_by',
                    field=models.UUIDField(null=True),
                ),
            ]



#### HOLIDAY MODLE

    # last migration in 'MASTER' branch  '0003_alter_holiday_is_delete.py' 
    # last migration in 'SANDBOX' branch "0005_remove_holiday_is_delete_holiday_deleted_by.py"

    ### REMOVED_FIELDS: is_delete

    ### ADDED_FIELD: deleted_by

    ### MODIFIED_FIELD: branch_uuid, company_uuid,

    ### CHANGES:

        # 0004_alter_holiday_branch_uuid_alter_holiday_company_uuid.py
        operations = [
                migrations.AlterField(
                    model_name='holiday',
                    name='branch_uuid',
                    field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='branch_holiday', to='branch.branch'),
                ),

                migrations.AlterField(
                    model_name='holiday',
                    name='company_uuid',
                    field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_holiday', to='company.company'),
                ),
            ]
        
        # 0005_remove_holiday_is_delete_holiday_deleted_by.py
        operations = [
                    migrations.RemoveField(
                        model_name='holiday',
                        name='is_delete',
                    ),
                    migrations.AddField(
                        model_name='holiday',
                        name='deleted_by',
                        field=models.UUIDField(null=True),
                    ),
                ]
                        



#### EMPLOYEE MODEL

    # last migration in 'MASTER' branch  '0024_employeeupdatehistory_employeebranchtransfer.py' 
    # last migration in 'SANDBOX' branch "0032_alter_employee_required_password_reset.py"

    ### NEW MODEL : EmployeeDocument

    ### EMPLOYEE

        ### REMOVED_FIELDS: is_delete, multiple_worklog

        ### ADDED_FIELD: deleted_by, worklog, workspace, otp_expired_at, required_password_reset,

        ### MODIFIED_FIELD: branch_uuid, company_uuid, employee_type, company_email, required_password_reset

        # unique_together IS REMOVED FROM EMPLOYEE MODEL
    
    ### TRAINEEIMAGE

        ### REMOVED_FIELDS: is_delete

        ### ADDED_FIELD: deleted_by


    ### EMPLOYEE_BRANCH_TRANSFER

        ### REMOVED_FIELDS: is_delete

        ### ADDED_FIELD: deleted_by
   


    ### CHANGES:

        # 0025_alter_employee_branch_uuid_and_more.py

         dependencies = [
                    ('branch', '0013_branch_dst_time'),
                    ('company', '0004_alter_company_is_delete'),
                    ('employee', '0024_employeeupdatehistory_employeebranchtransfer'),
                ]

        operations = [
                migrations.AlterField(
                    model_name='employee',
                    name='branch_uuid',
                    field=models.ForeignKey(null=True,on_delete=django.db.models.deletion.CASCADE, related_name='employee_branch', to='branch.branch'),
                ),
                migrations.AlterField(
                    model_name='employee',
                    name='company_uuid',
                    field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_company', to='company.company'),
                ),

                #### NEW MODEL


                migrations.CreateModel(
                    name='EmployeeDocuments',
                    fields=[
                        ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                        ('document_type', models.CharField(blank=True, choices=[('APPOINTMENT LETTER', 'Appointment Letter'), ('TERMINATION LETTER', 'Termination Letter'), ('CONTRACT', 'Contract'), ('PASSPORT', 'Passport'), ('RESUME', 'Resume'), ('NOC', 'Noc'), ('BRP', 'Brp'), ('ID', 'Id')], null=True)),
                        ('content', models.JSONField(blank=True, null=True)),
                        ('expires_at', models.DateTimeField(null=True)),
                        ('created_at', models.DateTimeField(auto_now_add=True)),
                        ('updated_at', models.DateTimeField(auto_now=True)),
                        ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_documents', to='employee.employee')),
                    ],
                ),
            ]


            # 0026_alter_employee_branch_uuid_and_more.py

            operations = [
                    migrations.AlterField(
                        model_name='employee',
                        name='branch_uuid',
                        field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee_branch', to='branch.branch'),
                    ),
                    migrations.AlterField(
                        model_name='employee',
                        name='company_uuid',
                        field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee_company', to='company.company'),
                    ),
                ]

            # 0027_remove_employee_multiple_worklog_employee_worklog_and_more.py    

             operations = [
                    migrations.RemoveField(
                        model_name='employee',
                        name='multiple_worklog',
                    ),
                    migrations.AddField(
                        model_name='employee',
                        name='worklog',
                        field=models.CharField(default='SINGLE', max_length=32),
                    ),
                    migrations.AddField(
                        model_name='employee',
                        name='workspace',
                        field=models.CharField(default='ON_SITE', max_length=32),
                    ),
                    migrations.AlterField(
                        model_name='employee',
                        name='employee_type',
                        field=models.CharField(default='FULL_TIME', max_length=32),
                    ),
                    migrations.AlterField(
                        model_name='employee',
                        name='company_email',
                        field=models.EmailField(max_length=128,unique=True)
                    )
                ]

            # 0028_alter_employee_unique_together.py    

            operations = [
                migrations.AlterUniqueTogether(
                    name='employee',
                    unique_together=set(),
                ),
                ]

            # 0029_remove_employee_is_delete_and_more.py  

            operations = [
                    migrations.RemoveField(
                        model_name='employee',
                        name='is_delete',
                    ),
                    migrations.RemoveField(
                        model_name='employeebranchtransfer',
                        name='is_delete',
                    ),
                    migrations.RemoveField(
                        model_name='traineeimage',
                        name='is_delete',
                    ),
                    migrations.AddField(
                        model_name='employee',
                        name='deleted_by',
                        field=models.UUIDField(null=True),
                    ),
                    migrations.AddField(
                        model_name='employeebranchtransfer',
                        name='deleted_by',
                        field=models.UUIDField(null=True),
                    ),
                    migrations.AddField(
                        model_name='traineeimage',
                        name='deleted_by',
                        field=models.UUIDField(null=True),
                    ),
                ]  

            # 0030_alter_employee_company_email.py  

            operations = [
                migrations.AlterField(
                    model_name='employee',
                    name='company_email',
                    field=models.EmailField(max_length=128),
                ),
            ]  

            # 0031_employee_otp_expired_at_and_more.py 

            operations = [
                migrations.AddField(
                    model_name='employee',
                    name='otp_expired_at',
                    field=models.DateTimeField(blank=True, null=True),
                ),
                migrations.AddField(
                    model_name='employee',
                    name='required_password_reset',
                    field=models.BooleanField(default=True),
                ),
            ]

            # 0032_alter_employee_required_password_reset.py 

            operations = [
                migrations.AlterField(
                    model_name='employee',
                    name='required_password_reset',
                    field=models.BooleanField(default=True, null=True),
                ),
            ]


#### LEAVE MODEL

    # last migration in 'MASTER' branch  '0008_alter_leaveapplication_leave_reason_and_more.py' 
    # last migration in 'SANDBOX' branch "0013_leaveapplication_primary_approval_comment.py"

    ### LEAVE_APPLICATION:

        ### REMOVED_FIELDS: is_delete

        ### ADDED_FIELD: deleted_by, attachments, primary_updated_at, primary_updated_by, secondary_updated_at, secondary_updated_by, primary_approval_comment

        ### MODIFIED_FIELD: branch_uuid, company_uuid,

    ### LEAVE_TYPE:

        ### REMOVED_FIELDS: is_delete

        ### ADDED_FIELD: deleted_by

        ### MODIFIED_FIELD: branch_uuid, company_uuid,    
    
    ### EMPLOYEE_LEAVE_DATE:

        ### REMOVED_FIELDS: is_delete

        ### ADDED_FIELD: deleted_by

       

    ### CHANGES:

        # 0009_alter_leaveapplication_branch_uuid_and_more.py 

        operations = [
            migrations.AlterField(
                model_name='leaveapplication',
                name='branch_uuid',
                field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branch_leave_application', to='branch.branch'),
            ),
            migrations.AlterField(
                model_name='leaveapplication',
                name='company_uuid',
                field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_leave_application', to='company.company'),
            ),
            migrations.AlterField(
                model_name='leavetype',
                name='branch_uuid',
                field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='branch_leave_type', to='branch.branch'),
            ),
            migrations.AlterField(
                model_name='leavetype',
                name='company_uuid',
                field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_leave_type', to='company.company'),
            ),
        ]

        # 0010_remove_employeeleavedate_is_delete_and_more.py

        operations = [
            migrations.RemoveField(
                model_name='employeeleavedate',
                name='is_delete',
            ),
            migrations.RemoveField(
                model_name='leaveapplication',
                name='is_delete',
            ),
            migrations.RemoveField(
                model_name='leavetype',
                name='is_delete',
            ),
            migrations.AddField(
                model_name='employeeleavedate',
                name='deleted_by',
                field=models.UUIDField(null=True),
            ),
            migrations.AddField(
                model_name='leaveapplication',
                name='deleted_by',
                field=models.UUIDField(null=True),
            ),
            migrations.AddField(
                model_name='leavetype',
                name='deleted_by',
                field=models.UUIDField(null=True),
            ),
        ]

        # 0011_leaveapplication_attachments.py

        operations = [
            migrations.AddField(
                model_name='leaveapplication',
                name='attachments',
                field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), default=list, null=True, size=None),
            ),
        ]
        
        # 0012_leaveapplication_primary_updated_at_and_more.py

        operations = [
            migrations.AddField(
                model_name='leaveapplication',
                name='primary_updated_at',
                field=models.DateTimeField(null=True),
            ),
            migrations.AddField(
                model_name='leaveapplication',
                name='primary_updated_by',
                field=models.CharField(max_length=50, null=True),
            ),
            migrations.AddField(
                model_name='leaveapplication',
                name='secondary_updated_at',
                field=models.DateField(null=True),
            ),
            migrations.AddField(
                model_name='leaveapplication',
                name='secondary_updated_by',
                field=models.CharField(max_length=50, null=True),
            ),
        ]

        # 0013_leaveapplication_primary_approval_comment.py

        operations = [
            migrations.AddField(
                model_name='leaveapplication',
                name='primary_approval_comment',
                field=models.TextField(blank=True, max_length=256, null=True),
            ),
        ]




#### MEETING EVENT MODEL

    # last migration in 'MASTER' branch  '0008_meetingevent_duration_and_more.py' 
    # last migration in 'SANDBOX' branch "0009_alter_meetingevent_branch_uuid_and_more.py"

    

    ### MODIFIED_FIELD: branch_uuid, company_uuid,  

    ### CHANGES:

        # 0009_alter_meetingevent_branch_uuid_and_more.py

        operations = [
            migrations.AlterField(
                model_name='meetingevent',
                name='branch_uuid',
                field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='branch_meeting', to='branch.branch'),
            ),
            migrations.AlterField(
                model_name='meetingevent',
                name='company_uuid',
                field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_meeting', to='company.company'),
            ),
        ]



#### NOTICE MODEL

    # last migration in 'MASTER' branch  '0008_notice_notice_to_team.py' 
    # last migration in 'SANDBOX' branch "0010_remove_notice_is_delete_notice_deleted_by.py"

    ### REMOVED_FIELDS: is_delete

    ### ADDED_FIELD: deleted_by

    ### MODIFIED_FIELD: branch_uuid, company_uuid,  

    ### CHANGES:

        # 0009_alter_notice_branch_uuid_alter_notice_company_uuid.py

        operations = [
            migrations.AlterField(
                model_name='notice',
                name='branch_uuid',
                field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='branch_notice', to='branch.branch'),
            ),
            migrations.AlterField(
                model_name='notice',
                name='company_uuid',
                field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_notice', to='company.company'),
            ),
        ]

        # 0010_remove_notice_is_delete_notice_deleted_by.py 

        operations = [
            migrations.RemoveField(
                model_name='notice',
                name='is_delete',
            ),
            migrations.AddField(
                model_name='notice',
                name='deleted_by',
                field=models.UUIDField(null=True),
            ),
        ]


#### ROLE MODEL 

    # last migration in 'MASTER' branch  '0008_notice_notice_to_team.py' 
    # last migration in 'SANDBOX' branch "0012_remove_permission_is_delete_remove_role_is_delete_and_more.py"

    ### ROLE:
        ### REMOVED_FIELDS: is_delete

        ### ADDED_FIELD: deleted_by

        ### MODIFIED_FIELD: branch_uuid, company_uuid,  

    ### PERMISSIONS:
        ### REMOVED_FIELDS: is_delete

        ### ADDED_FIELD: deleted_by     

    ### CHANGES:

        # 0011_alter_role_branch_uuid_alter_role_company_uuid.py

        operations = [
                migrations.AlterField(
                    model_name='role',
                    name='branch_uuid',
                    field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='branch_role', to='branch.branch'),
                ),
                migrations.AlterField(
                    model_name='role',
                    name='company_uuid',
                    field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_role', to='company.company'),
                ),
            ]

        # 0012_remove_permission_is_delete_remove_role_is_delete_and_more.py    

        operations = [
            migrations.RemoveField(
                model_name='permission',
                name='is_delete',
            ),
            migrations.RemoveField(
                model_name='role',
                name='is_delete',
            ),
            migrations.AddField(
                model_name='permission',
                name='deleted_by',
                field=models.UUIDField(null=True),
            ),
            migrations.AddField(
                model_name='role',
                name='deleted_by',
                field=models.UUIDField(null=True),
            ),
        ]

#### TEAM MODEL

    # last migration in 'MASTER' branch  '0005_rename_team_leads_team_team_lead.py' 
    # last migration in 'SANDBOX' branch "0006_remove_team_is_delete_team_deleted_by.py"

    ### REMOVED_FIELDS: is_delete

    ### ADDED_FIELD: deleted_by

    ### CHANGES:

        # 0006_remove_team_is_delete_team_deleted_by.py

        operations = [
            migrations.RemoveField(
                model_name='team',
                name='is_delete',
            ),
            migrations.AddField(
                model_name='team',
                name='deleted_by',
                field=models.UUIDField(null=True),
            ),
        ]


 




    


            





        
        