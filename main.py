# 1. 변수 선언 및 초기값 설정
allowance = 600000
weekly_total = 120000 * 4  # 480,000
housing_sub_monthly = 20000
music_app = 7900
netflix = 4900
coupang = 7890
icloud = 3900

print("======= 💰 대학생 자산 관리 매니저 (1단계) =======")

# 2. 사용자 입력 (Input)
part_time_pay = int(input("이번 달 알바비를 입력하세요: "))
elec_bill = int(input("이번 달 전기세를 입력하세요: "))
gas_bill = int(input("이번 달 가스비를 입력하세요: "))

# 청약 정보 입력 (현재 61회, 1220000원 기준)
current_sub_count = int(input("현재까지의 청약 납입 횟수를 입력하세요: "))
current_sub_balance = int(input("현재까지의 청약 총 잔액을 입력하세요: "))

# 3. 계산 과정 (Process)
total_income = allowance + part_time_pay
fixed_expenses = (weekly_total + housing_sub_monthly + music_app + 
                  netflix + coupang + icloud + elec_bill + gas_bill)

remained_money = total_income - fixed_expenses

# 주식 70%, 비상금 30% 계산
invest_amount = remained_money * 0.7
emergency_fund = remained_money * 0.3

# 청약 업데이트
new_sub_count = current_sub_count + 1
new_sub_balance = current_sub_balance + housing_sub_monthly

# 4. 결과 출력 (Output)
print("\n" + "="*40)
print(f"📊 이번 달 총 수입: {total_income:,}원")
print(f"💸 이번 달 고정 지출: {fixed_expenses:,}원")
print(f"🧧 남은 잔액: {remained_money:,}원")
print("-" * 40)
print(f"📈 [주식 투자] 가능 금액 (70%): {invest_amount:,.0f}원")
print(f"🚨 [비상금] 저축 금액 (30%): {emergency_fund:,.0f}원")
print("-" * 40)
print(f"🏠 주택청약 업데이트 정보")
print(f"   - 이번 달 납입 횟수: {new_sub_count}회")
print(f"   - 현재 청약 총 잔액: {new_sub_balance:,}원")
print("="*40)
