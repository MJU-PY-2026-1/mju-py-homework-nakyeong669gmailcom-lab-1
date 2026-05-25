# 1. 변수 선언 및 초기값 설정
allowance = 600000
weekly_total = 120000 * 4  # 480,000
housing_sub_monthly = 20000
music_app = 7900
netflix = 4900
coupang = 7890
icloud = 3900
fixed_expenses = weekly_total + housing_sub_monthly + music_app + netflix + coupang + icloud

# 프로그램 실행 중에 계속 유지하고 업데이트할 전역 변수들
part_time_pay = 0
elec_bill = 0
gas_bill = 0
current_sub_count = 0
current_sub_balance = 0 

total_income = 0
remained_money = 0
invest_amount = 0
savings_amount = 0
new_sub_count = 0
new_sub_balance = 0

# 2. 함수 정의
def input_user_data():
      print("\n---[ 2. 사용자 입력(Input) ]---")
      p_pay = int(input("이번 달 알바비를 입력하세요: "))
      e_bill = int(input("이번 달 전기세를 입력하세요: "))
      g_bill = int(input("이번 달 가스비를 입력하세요: "))
      c_count = int(input("현재까지의 청약 납입 횟수를 입력하세요: "))
      c_balance = int(input("현재까지의 청약 총 잔액을 입력하세요: "))

      return p_pay, e_bill, g_bill, c_count, c_balance

def process_asset_calculation(p_pay, e_bill, g_bill, c_count, c_balance):
      global part_time_pay, elec_bill, gas_bill, current_sub_count, current_sub_balance
      global total_income,fixed_expenses, remained_money, invest_amount, savings_amount, new_sub_count, new_sub_balance
    
      part_time_pay = p_pay
      elec_bill = e_bill
      gas_bill = g_bill
      current_sub_count = c_count
      current_cub_count = c_balance

      total_income = allowance + part_time_pay
      fixed_expenses = (weekly_total + housing_sub_monthly + music_app + 
                  netflix + coupang + icloud + elec_bill + gas_bill)

      remained_money = total_income - fixed_expenses

      # [2단계 로직: 조건문 및 선택 시스템]
      invest_amount = 0
      savings_amount = 0

      print("\n---[투자 성향 선택]---")
      print("1: 안정형(30%) | 2: 수익형(60%) | 3: 공격형(90%)")
      choice = int(input("투자 번호를 선택하세요: "))

      #다중 조건문 & 중첩 조건문 & 논리 연산자 활용
      if remained_money < 0:
          print("⚠️ 경고: 적자 상태입니다. 투자가 불가능합니다.")
      else:
          if choice == 1 and remained_money >= 100000:
              invest_amonut = remained_money * 0.3
              savings_amount = remained_money - invest_amount
          elif choice == 2 and remained_money >= 200000:
              invest_amount = remained_money * 0.6
              savings_amount = remained_money - invest_amount
          elif choice == 3 and remained_money >= 300000:
              invest_amount = remained_money * 0.9
              savings_amount = remained_money - invest_amount
          else:
              print("🚫 잔액이 부족하거나 잘못된 선택입니다.")
              savings_amount = remained_money

      # 청약 업데이트
      new_sub_count = current_sub_count + 1
      new_sub_balance = current_sub_balance + housing_sub_monthly

def output_asset_result():
      print("\n" + "="*40)
      print(f"📊 이번 달 총 수입: {total_income:,}원")
      print(f"💸 이번 달 고정 지출: {fixed_expenses:,}원")
      print(f"🧧 남은 잔액: {remained_money:,}원")
      print("-" * 40)

      print(f"📈 [투자] 실행 금액 (70%): {invest_amount:,.0f}원")
      print(f"🚨 [비상금] 저축 금액 (30%): {savings_amount:,.0f}원")
      print("-" * 40)

      print(f"🏠 주택청약 업데이트 정보")
      print(f"   - 이번 달 납입 횟수: {new_sub_count}회")
      print(f"   - 현재 청약 총 잔액: {new_sub_balance:,}원")
      print("="*40)

 # 3. 메인 로직 (while True 무한 루프)

print("======= 💰 대학생 자산 관리 매니저 (3차과제 v2.0) =======")

while True:
      print("\n[ 메인 메뉴 ]")
      print("1. 자산 관리 시작 (입력, 계산, 결과 출력)")
      print("2. 프로그램 종료")
      print("-" * 40)

      choice_menu = int(input("원하는 메뉴 번호를 선택하세요: "))

      if choice_menu == 1:
            p_pay, e_bill, g_bill, c_count, c_balance = input_user_data()

            process_asset_calculation(p_pay, e_bill, g_bill, c_count, c_balance)

            output_asset_result()
      elif choice_menu == 2:
            print(("\n👋 프로그램을 종료합니다. 이용해 주셔서 감사합니다!"))
            break
      else:
            print("❌ 올바른 메뉴 번호(1~2)를 입력해주세요.")
