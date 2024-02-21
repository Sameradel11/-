# Generated by Django 4.2.10 on 2024-02-21 05:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('Admission_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Start_Date', models.DateTimeField(default=django.utils.timezone.now)),
                ('End_Date', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('Appointment_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('Doctor_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=30)),
                ('Specialization', models.CharField(max_length=20)),
                ('Phone_Number', models.CharField(max_length=14)),
                ('Appointment_Price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('Employee_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=30)),
                ('Phone_Number', models.CharField(max_length=14)),
                ('Role', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('Patient_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=30)),
                ('Address', models.CharField(max_length=100)),
                ('Phone_Number', models.CharField(max_length=14)),
                ('Date_Of_Birth', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('Room_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Room_Number', models.CharField(max_length=20)),
                ('Room_Type', models.CharField(max_length=20)),
                ('Room_Price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TreatmentAdmission',
            fields=[
                ('Treatment_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Treatment_Title', models.CharField(max_length=255)),
                ('Treatment_Details', models.TextField(max_length=255)),
                ('DateTime', models.DateTimeField(auto_now_add=True)),
                ('price', models.IntegerField()),
                ('admission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.admission')),
            ],
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('Treatment_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Procedure', models.CharField(max_length=255)),
                ('Disease', models.CharField(max_length=255)),
                ('Appointment_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.appointment')),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('Bill_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Date', models.DateTimeField(auto_now_add=True)),
                ('Status', models.CharField(max_length=10)),
                ('Total', models.IntegerField()),
                ('Reason', models.CharField(default='Reason', max_length=255)),
                ('Patient_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.patient')),
            ],
        ),
        migrations.AddField(
            model_name='appointment',
            name='Doctor_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.doctor'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='Patient_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.patient'),
        ),
        migrations.AddField(
            model_name='admission',
            name='Doctor_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.doctor'),
        ),
        migrations.AddField(
            model_name='admission',
            name='Patient_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.patient'),
        ),
        migrations.AddField(
            model_name='admission',
            name='Room_Number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.room'),
        ),
        migrations.CreateModel(
            name='Employee_Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employee_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.employee')),
                ('Room_Number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.room')),
            ],
            options={
                'unique_together': {('Employee_ID', 'Room_Number')},
            },
        ),
    ]
