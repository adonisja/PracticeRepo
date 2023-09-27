#include <iostream>
#include <climits>
#include <array>
#include <iomanip>
using namespace std;

int main()
{
    /*BMI calculator
    weight(kg) / height(m) * height(m)
    Underweight: < 18.5
    Normal weight: 18.5 - 24.9
    Overweight: > 25
    */
   float weight_kg = 0, weight_lbs = 0, height_m = 0, height_ft = 0, bmi = 0;
   float underweight = 18.5, normalweight = 24.9, overweight = 25;
   string system;

   cout << "Do you use the metric or imperial system? ";
   cin >> system;
   if (system == "metric")
   {
        cout << "Enter your weight in kg: ";
        cin >> weight_kg;
        cout << "Enter your height in meters: ";
        cin >> height_m;
   
        height_ft = height_m * 3.28084;
        weight_lbs = weight_kg * 2.20462;
   
        bmi = weight_kg / (height_m * height_m);

        if (bmi < underweight)
        {
            cout << "You are underweight" << "\n";
            cout << "Your BMI is: " << bmi << "\n";
            cout << "Your weight in lbs is: " << fixed << setprecision(2) << weight_lbs << "\n";
            cout << "Your height in ft is: " << fixed << setprecision(2) << height_ft << "\n";
        }
        else if (bmi > underweight && bmi < normalweight)
        {
            cout << "You are normal weight" << "\n";
            cout << "Your BMI is: " << bmi << "\n";
            cout << "Your weight in lbs is: " << fixed << setprecision(2) << weight_lbs << "\n";
            cout << "Your height in ft is: " << fixed << setprecision(2) << height_ft << "\n";
        }
        else
        {
            cout << "You are overweight" << "\n";
            cout << "Your BMI is: " << bmi << "\n";
            cout << "Your weight in lbs is: " << fixed << setprecision(2) << weight_lbs << "\n";
            cout << "Your height in ft is: " << fixed << setprecision(2) << height_ft << "\n";
        }

   }
   else if(system == "imperial")
   {
        cout << "Enter your weight in lbs: " << "\n";
        cin >> weight_lbs;
        cout << "Enter your height in ft: " << "\n";
        cin >> height_ft;

        weight_kg = weight_lbs * 0.453592;
        height_m = height_ft * 0.3048;

        bmi = weight_kg / (height_m * height_m);

        if (bmi < underweight)
        {
            cout << "You are underweight" << "\n";
            cout << "Your BMI is: " << bmi << "\n";
            cout << "Your weight converted to kilograms(kg) is: " << fixed << setprecision(2) << weight_kg << "\n";
            cout << "Your height converted meters(m) is: " << fixed << setprecision(2) << height_m << "\n";
        }
        else if (bmi > underweight && bmi < normalweight)
        {
            cout << "You are normal weight" << "\n";
            cout << "Your BMI is: " << bmi << "\n";
            cout << "Your weight converted to kilograms(kg) is: " << fixed << setprecision(2) << weight_kg << "\n";
            cout << "Your height converted to meters(m) is: " << fixed << setprecision(2) << height_m << "\n";
        }
        else
        {
            cout << "You are overweight" << "\n";
            cout << "Your BMI is: " << bmi << "\n";
            cout << "Your weight converted to kilograms(kg) is: " << fixed << setprecision(2) << weight_kg << "\n";
            cout << "Your height converted to meters(m) is: " << fixed << setprecision(2) << height_m << "\n";
        }
    }
    else
    {
        cout << "Invalid input! Incorrect Measurement System inputted";
    }
   
    
    return 0;
}