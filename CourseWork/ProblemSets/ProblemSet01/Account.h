#ifndef ACCOUNT_H
#define ACCOUNT_H

#include <iostream>
#include <iomanip>
#include <string>
#include <sstream>


class Account
{
    private:
        std::string number;
        std::string pin;
        double balance;

    public:
        Account()
        {
            number = 111111111l;
            pin = 1234;
            balance = 100.00;
        }
        
        Account (const Account &obj)
        {
            number = obj.number;
            pin = obj.pin;
            balance = obj.balance;
        }

        Account& operator=(const Account &rhs)
        {
            if (this != &rhs)
            {
                number = rhs.number;
                pin = rhs.pin;
                balance = rhs.balance;
            }
            return *this;
        }

        ~Account() {}

        std::string GetNumber()
        {
            return number;
        }

        std::string GetPin()
        {
            return pin;
        }

        double GetBalance()
        {
            return balance;
        }

        void SetNumber(std::string value)
        {
            if (value.length() == 16)
            {
                number = value;
            }
        }
        void SetPin(std::string value)
        {
            if (value.length() == 4)
            {
                pin = value;
            }
        }

        void Deposit(double value)
        {
            if (value > 0)
            {
                balance += value;
            }
        }

        void Withdraw(double value)
        {
            if (value > 0 && balance >= value)
            {
                balance -= value;
            }
        }

        std::string ToString() const
        {
           std::stringstream out;
           out << std::fixed << std::setprecision(2); 
           out << "Account: " << number << "\n";
           out << "Pin: ****";
           out << "$" << balance;
        }

        friend std::ostream& operator<<(std::ostream& out, const Account& obj)
        {
            out << obj.ToString();
            return out;
        }
        
}



#endif
