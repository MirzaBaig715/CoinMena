import time

from schedule import Scheduler
import threading

from alpha_vantage.foreignexchange import ForeignExchange

from CoinMena import settings
from crypto_metrics.models import AlphaVantage
from crypto_metrics.utils.common import format_data


def get_exchange_rates():
    fe = ForeignExchange(key=settings.ALPHA_API_KEY)
    # fetches the price of BTC/USD from the alphavantage API every hour, and stores it on postgres.
    # There is no metadata in this call
    data, _ = fe.get_currency_exchange_rate(from_currency='BTC', to_currency='USD')
    formatted_data = format_data(data)
    AlphaVantage.objects.create(**formatted_data)
    print('=========== Scheduling is working ==========')

def run_continuously(self, interval=1):
    """Continuously run, while executing pending jobs at each elapsed
    time interval.
    @return cease_continuous_run: threading.Event which can be set to
    cease continuous run.
    Please note that it is *intended behavior that run_continuously()
    does not run missed jobs*. For example, if you've registered a job
    that should run every minute and you set a continuous run interval
    of one hour then your job won't be run 60 times at each interval but
    only once.
    """

    cease_continuous_run = threading.Event()

    class ScheduleThread(threading.Thread):

        @classmethod
        def run(cls):
            while not cease_continuous_run.is_set():
                self.run_pending()
                time.sleep(interval)

    continuous_thread = ScheduleThread()
    continuous_thread.setDaemon(True)
    continuous_thread.start()
    return cease_continuous_run

Scheduler.run_continuously = run_continuously

def start_scheduler():
    scheduler = Scheduler()
    scheduler.every().hour.do(get_exchange_rates)
    scheduler.run_continuously()
