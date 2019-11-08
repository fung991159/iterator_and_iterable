#Investment related
#calculate investmnet period required
import datetime, math

#just some dummy number ;)
capital = 1_000_000
target_capital = 1_0000_000
return_rate = 7 * 0.01

num_year_required = math.log(target_capital/capital) / math.log(1+return_rate)
num_year_required = round(num_year_required, 2)

curr_year = datetime.date.today().year
end_year = math.ceil(curr_year + num_year_required)
end_capital = capital

print()
print(f'By investing ${capital:,} with {return_rate*100:.2f}% return each year\n\
It will takes {num_year_required} year(s) to reach ${target_capital:,}')
print()

#for printing details investment return each year
while end_capital < target_capital:
    end_capital *= (1 + return_rate)
    end_capital = round(end_capital, 2)

    curr_year +=1
    print(f'{curr_year}\t{end_capital:,.2f}')





