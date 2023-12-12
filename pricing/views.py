
from rest_framework import generics
from rest_framework.response import Response

from pricing.models import Prices
from pricing.serializers import PricesSerializer


class PricesCreateAPIView(generics.CreateAPIView):
    queryset = Prices.objects.all()
    serializer_class = PricesSerializer
    def create(self, request, *args, **kwargs):
        try:
            # Проверка статуса пользователя
            if not request.user.login_as and not request.user.is_superuser :
                return Response({'error': 'У вас нет статуса продавец'}, status=403)

            # Получение цены товара из запроса
            original_price = request.data.get('original_price')

            # Расчет всех надбавок
            tax = 0.06 * original_price
            bank_commission = 0.02 * original_price
            transfer_commission = 0.2 * original_price

            # Итоговая цена с учетом всех надбавок
            total_price = round(original_price + tax + bank_commission + transfer_commission,2)

            # Сериализация данных
            serializer = self.get_serializer(data={'original_price': original_price,'total_price': total_price})
            serializer.is_valid(raise_exception=True)

            # Возвращение результата в формате JSON
            return Response(serializer.data)

        except Exception as e:
            return Response({'error': str(e)}, status=400)